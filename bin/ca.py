from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
import json
api_key = 'P07AGweMSPUbYdEciorS1AVCRBhcrmcFXZE4HtCPFE49cpcZ8WmXsY0Lp7QeLon0'
api_secret = 'IMo7JeJShx8kKYFz4hhgkFgKMymXdbg5Vn1rRvene26jZo5l3b6sLC64BNBcY2RU'
api_host = 'https://fapi.binance.com'

def tojson(data):
    data = json.dumps(data, default=lambda obj: obj.__dict__)
    data = json.loads(data)
    return data

request_client = RequestClient(url=api_host, api_key=api_key, secret_key=api_secret)

result = request_client.get_candlestick_data(symbol="ETHBUSD", interval='15m', startTime=None, endTime=None, limit=100)

# print(tojson(result))

k_list = tojson(result)


def c_ma(data,interval,price='Close'):
    MA = []
    for i in range(len(data)):
        total = 0
        for j in range(interval):
            if (i-interval+1) >=0:
                total+=float(data[i-j][price])
            else:
                break
        MA.append(float('%.3f'% (total/interval)))
    return MA

MA = c_ma(k_list,9,'close')
print(MA)

def c_ema(data,ma,interval,price='Close'):
    EMA = []
    a = 2/(interval+1)
    firseEMA = False
    for i in range(len(ma)):
        if ma[i]>0:
            if not firseEMA:
                firseEMA = True
                EMA.append(ma[i])
            else:
                EMA.append(float('%.3f'% (a*float(data[i][price])+(1-a)*EMA[i-1])))
        else:
            EMA.append(ma[i])
    return EMA

EMA = c_ema(k_list,MA,9,'close')
print(EMA)

