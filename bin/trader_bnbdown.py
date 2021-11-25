from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
# from lib import Utility
from lib import Logger
# from enum import Enum
import logging
import time 
import configparser
import json
import redis   
import datetime
import requests
import traceback


# 读取配置文件
CONFIG = configparser.RawConfigParser()
CONFIG.read('../config/config.ini')


# 参数
beginPrice = 620
endPrice = 640
distance = 1
pointProfit = 1
amount = 0.02
symbol = 'BNBBUSD'
api_key = 'P07AGweMSPUbYdEciorS1AVCRBhcrmcFXZE4HtCPFE49cpcZ8WmXsY0Lp7QeLon0'
api_secret = 'IMo7JeJShx8kKYFz4hhgkFgKMymXdbg5Vn1rRvene26jZo5l3b6sLC64BNBcY2RU'
api_host = 'https://fapi.binance.com'
leverage = 5


# redis配置
redis_host = CONFIG.get('redis', 'host')
redis_port = CONFIG.get('redis', 'port')
redis_password = CONFIG.get('redis', 'password')

# 全局变量
arrNet = []
arrMsg = []
acc = None
account_key = 'future_trader_account_'


class FutureTrader:

    def __init__(self): 

        self.http_client = RequestClient(url=api_host, api_key=api_key, secret_key=api_secret)
        # self.redis = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)
        
        self.trader_name = 'future_trader_t'
        self.account_key = account_key + self.trader_name
        logger = Logger.Logger()
        self.logger = logger.getLogger(self.trader_name)

        #调整开仓杠杆
        self.http_client.change_initial_leverage(symbol=symbol,leverage=leverage)
    
    def findOrder (self, orderId, NumOfTimes, ordersList = []) :
        for j in range(NumOfTimes) :    
            orders = None
            if len(ordersList) == 0:
                orders = self.getOrders()
            else :
                orders = ordersList
            for i in range(len(orders)):
                if orderId == orders[i]["clientOrderId"]:
                    return orders[i]
            order = self.checkOrder(orderId)
            if order:
                return order
        return None

    def checkOrder (self, orderId) :
        check_order = self.http_client.get_order(symbol, origClientOrderId = orderId)
        if check_order :
            check_order = self.tojson(check_order)
            return check_order
        return False

    def cancelOrder (self, orders, price, side) :
        for i in range(len(orders)) : 
            if price == orders[i]["price"] and side == orders[i]["side"]:
                order = self.http_client.cancel_order(orders[i]['symbol'],
                        origClientOrderId = orders[i]['clientOrderId'])
                if order :
                    self.logger.info("=====取消订单成功======="+orders[i]['clientOrderId'])
                else :
                    self.logger.info("=====取消订单失败======="+orders[i]['clientOrderId'])

    def checkOpenOrders (self, orders, ticker_price):
        global arrNet
        for i in range(len(arrNet)): 
            if arrNet[i]["id"] == -1:
                continue
            if arrNet[i]["state"] != "pending":
                continue
            
            check_order = self.findOrder(arrNet[i]["id"], 1, orders)
                
            if check_order.get('status') == "CANCELED":
                arrNet[i]["state"] = "cover"
                #arrNet[i]['id'] = -1
                self.logger.info("buy order status was canceled: "+check_order.get('status'))

            elif check_order.get('status') == "FILLED": 
                #self.logger.info('=========sell============')
                #下单

                price = float(arrNet[i]["coverPrice"])
                if(ticker_price < price):
                    price = ticker_price

                sell_order_params = {
                    'symbol': symbol,
                    'side': 'BUY',
                    'ordertype': 'LIMIT',
                    'timeInForce': 'GTC',
                    'quantity': check_order.get('origQty'),
                    'price': price
                }
                print(sell_order_params)
                sell_order = self.http_client.post_order(**sell_order_params)
                sell_order = self.tojson(sell_order)
                self.logger.info('=====买单=====  ' + json.dumps(sell_order))
                if sell_order:
                    arrNet[i]["state"] = "cover"
                    arrNet[i]["id"] = sell_order.get('clientOrderId')  
                else :
                    # 撤销
                    # self.cancelOrder(arrNet[i]["coverPrice"], "SELL")
                    self.logger.info("=====挂买单失败=====" + json.dumps(arrNet[i]))
                account = self.getAccount() 

            elif check_order.get('status') == "NEW":
                pass
                # timestamp = time.time() - 3600 * 3
                # if int(check_order.get('updateTime') / 1000) < timestamp:
                #     print(arrNet[i]["id"])
                #     order = self.http_client.cancel_order(symbol, origClientOrderId = arrNet[i]["id"])
                #     self.logger.info("buy order status is: to be canceled")
                #else: 
                    #self.logger.info("buy order status is: New")
            else:
                self.logger.info("buy order status is not above options: "+check_order.get('status'))
            pass


    def checkCoverOrders (self, orders) :   
        global arrNet
        for i in range(len(arrNet)): 
            #if not self.findOrder(arrNet[i]["id"], 1, orders) and arrNet[i]["state"] == "cover" :
            if arrNet[i]["state"] == "cover" :
                sell_order = self.findOrder(arrNet[i]["id"], 1, orders)
                #print(i, arrNet[i]["id"], sell_order)
                if sell_order and (sell_order.get('status') == "FILLED" or sell_order.get('status') == "CANCELED"):
                    print("removing: " +  sell_order.get('clientOrderId'))
                    #sell_order = > time.time()
                    arrNet[i]["id"] = -1
                    arrNet[i]["state"] = "idle"
                    #self.logger.info("====节点平仓，重置为空闲状态。===="+json.dumps(arrNet[i])) 

    def getOrders (self):
        orders = [] 
        #orders_data = self.http_client.get_orders(symbol, limit = 20)
        orders_data = self.http_client.get_open_orders(symbol)
        orders = self.tojson(orders_data)
        return orders


    def getTickerPrice(self):
        ticker_price = 0
        print(symbol)
        ticker = self.http_client.get_symbol_orderbook_ticker(symbol)
        if ticker:
            ticker = self.tojson(ticker)
            ticker_price = float(ticker[0].get('bidPrice', 0))
        return ticker_price
    
    def getAccount(self):
        account = self.http_client.get_account_information_v2()
        account = self.tojson(account)
        #print(account)
        return account

    def tojson(self,data):
        data = json.dumps(data, default=lambda obj: obj.__dict__)
        data = json.loads(data)  
        return data

    def onTick (self) :
        global arrNet
        ticker_price = self.getTickerPrice()
        orders = self.getOrders() 
        
        self.logger.info('=======ticker_price======='+str(ticker_price))
        for i in range(len(arrNet)):
            if i != 0 and arrNet[i]["state"] == "idle" and ticker_price < arrNet[i]["price"] and ticker_price >= arrNet[i - 1]["price"]:
                self.logger.info('==========buy===============')

                account = self.getAccount()
                a_usdt = 0
                if account:
                    assets = account.get('assets')
                    for obj in assets:
                        if obj.get('asset') == 'BUSD':
                            a_usdt = obj.get('availableBalance')
                            break

                print(a_usdt)
                if float(a_usdt) - float(arrNet[i]["price"]) * amount < 0 :
                    self.logger.info('余额不足，usdt='+str(a_usdt))
                    break

                buy_order_params = {
                    'symbol': symbol,
                    'side': 'SELL',
                    'ordertype': 'LIMIT',
                    'timeInForce': 'GTC',
                    'quantity': amount,
                    'price': float(arrNet[i]["price"])
                }
                print('=====================')
                print(buy_order_params)

                buy_order = self.http_client.post_order(**buy_order_params)
                buy_order = self.tojson(buy_order)
                self.logger.info('=====卖单=====  ' + json.dumps(buy_order))
                if buy_order: 
                    arrNet[i]["state"] = "pending"
                    arrNet[i]["id"] = buy_order.get('clientOrderId')
                else :
                    self.logger.info("=======挂卖单失败!======" + json.dumps(arrNet[i]))
                
                account = self.getAccount() 
        
        orders = self.getOrders() 
        #time.sleep(1)
        # 遍历买单
        self.checkOpenOrders(orders, ticker_price) 
        # 遍历买单
        #time.sleep(1)
        self.checkCoverOrders(orders) 

if __name__ == '__main__': 
    
    for i in range(int((endPrice - beginPrice) / distance)):
        arrNet.append({
            "price" : beginPrice + i * distance,
            "amount" : amount,
            "state" : "idle",    # pending / cover / idle
            "coverPrice" : beginPrice + i * distance - pointProfit,
            "id" : -1,
        })

    logger = Logger.Logger()
    log_name = 'error_trader_t'
    logger = logger.getLogger(log_name)

    futureTrader = FutureTrader()
    account = futureTrader.getAccount()
    while True:
        try:
            futureTrader.onTick()
            time.sleep(1)

        except Exception as e:
            logger.info("catch error: "+ str(e))
            print('str(e):\t', e)
            print('repr(e):\t', repr(e))
            print('traceback.format_exc():\n%s' % traceback.format_exc()) #字符串
            traceback.print_exc() #执行函
            time.sleep(5)
