from binance_f import RequestClient
from binance_f.constant.test import *
import json

def tojson(data):
    data = json.dumps(data, default=lambda obj: obj.__dict__)
    data = json.loads(data)  
    return data


url = "https://fapi.binance.com"
g_api_key = "P07AGweMSPUbYdEciorS1AVCRBhcrmcFXZE4HtCPFE49cpcZ8WmXsY0Lp7QeLon0"
g_secret_key = "IMo7JeJShx8kKYFz4hhgkFgKMymXdbg5Vn1rRvene26jZo5l3b6sLC64BNBcY2RU"

request_client = RequestClient(url=url,api_key=g_api_key, secret_key=g_secret_key)
result = request_client.get_balance_v2()
print(tojson(result))
