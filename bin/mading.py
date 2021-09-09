

stop_profit = 1.005   # 止盈
buy_point = 0.995 # 买入点
stop_loss = 0.9  # 止损
first_amount = 0.003
max_count = 4
current_count = 0
current_multiple = 1

profit_id = None # 止盈id
point_id = None # 买入id

# 127份
buy_points = [
    { "1": 0.001 },
    { "0.99": 0.002 },
    { "0.98": 0.004 },
    { "0.97": 0.008 },
    { "0.95": 0.016 },
    { "0.92": 0.032 },
    { "0.87": 0.064 }
]
current_point_index = 0

def pickPosition():
    _position = exchange.GetPosition()
    #Log(_position)
    for i in range(len(_position)):
        if _position[i]["Info"]["symbol"] == "ETHUSDT":
            return _position[i]
    return None

def checkOrder(order_id):
    if order_id:
        order = exchange.GetOrder(order_id)
        if order and order["Info"]["status"] == "FILLED": # 成交了
            return True
    return False

def handOrder():
    global stop_profit,buy_point,profit_id,point_id,current_count,max_count,current_multiple,first_amount,current_point_index

    current_point_index+=1
    if current_count > len(buy_points): return
    position = pickPosition()
    if position:
        entryPrice = float(position["Info"]["entryPrice"])
        markPrice = float(position["Info"]["markPrice"])
        positionAmt = float(position["Info"]["positionAmt"])

        profit_price = float('%.2f' % (entryPrice*stop_profit)) # 止盈价
        buy_price = float('%.2f' % (entryPrice*buy_point)) # 买入价

        exchange.SetDirection("buy")
        point_id = exchange.Buy(buy_price, positionAmt*current_multiple) # 向下挂一个买入价
        Log('向下挂一个买入价',buy_price,positionAmt*current_multiple)

        exchange.SetDirection("closebuy")
        profit_id = exchange.Sell(profit_price, positionAmt) # 向上挂一个止盈价
        Log('向上挂一个止盈价',profit_price,positionAmt)

def onTick():
    global stop_profit,buy_point,stop_loss,first_amount,max_count,current_count,current_multiple,profit_id,point_id,buy_points,current_point_index
    position = pickPosition()
    LogStatus(_D(), position, profit_id, point_id)

    if not position and not point_id and not profit_id: # 没有持仓也没有买入卖出单

        current_point = buy_points[current_point_index]
        for p in current_point:
            buy_amount = current_point[p]
        ticker = _C(exchange.GetTicker)
        exchange.SetDirection("buy")
        exchange.Buy(-1, buy_amount,ticker)
        Log('空仓买入.')
        handOrder()
    elif position:
        entryPrice = float(position["Info"]["entryPrice"])
        markPrice = float(position["Info"]["markPrice"])
        positionAmt = float(position["Info"]["positionAmt"])

        if entryPrice > markPrice and markPrice/entryPrice < stop_loss: # 止损
            exchange.SetDirection("closebuy")
            exchange.Sell(-1, positionAmt, markPrice, entryPrice)
            Log('止损',markPrice,entryPrice)
            profit_id = None
            point_id = None
            current_count = 0
            current_multiple = 1
        if checkOrder(point_id): # 买入了
            Log('买入了',point_id)
            if profit_id:
                exchange.CancelOrder(profit_id)
                profit_id = None
            point_id = None
            handOrder()
    if checkOrder(profit_id): # 止盈了
        Log('止盈了',profit_id)
        if point_id:
            exchange.CancelOrder(point_id)
            point_id = None
        profit_id = None
        current_count = 0
        current_multiple = 1

def main():
    exchange.SetContractType("swap")
    exchange.SetMarginLevel(1)
    while True:
        onTick()
        Sleep(500)