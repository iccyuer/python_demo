from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

api_key = 'P07AGweMSPUbYdEciorS1AVCRBhcrmcFXZE4HtCPFE49cpcZ8WmXsY0Lp7QeLon0'
api_secret = 'IMo7JeJShx8kKYFz4hhgkFgKMymXdbg5Vn1rRvene26jZo5l3b6sLC64BNBcY2RU'
api_host = 'https://fapi.binance.com'

request_client = RequestClient(url=api_host, api_key=api_key, secret_key=api_secret)

result = request_client.get_candlestick_data(symbol="ETHBUSD", interval='15min', startTime=None, endTime=None, limit=10)

print(result)