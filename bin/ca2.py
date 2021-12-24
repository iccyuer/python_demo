import math
# 9
# 14
# k_list = [
# {'Time': 1638201600000, 'Open': 57123.33, 'High': 57475.5, 'Low': 57000.99, 'Close': 57470.62, 'Volume': 1293.02213, 'OpenInterest': 0.0}, 
# {'Time': 1638205200000, 'Open': 57467.79, 'High': 58774.5, 'Low': 57415.37, 'Close': 58621.73, 'Volume': 4063.36645, 'OpenInterest': 0.0},
# {'Time': 1638208800000, 'Open': 58621.73, 'High': 58857.88, 'Low': 58484.87, 'Close': 58633.1, 'Volume': 1403.66706, 'OpenInterest': 0.0}, 
# {'Time': 1638212400000, 'Open': 58637.24, 'High': 58654.55, 'Low': 57786.94, 'Close': 57869.99, 'Volume': 1817.74925, 'OpenInterest': 0.0}, 
# {'Time': 1638216000000, 'Open': 57877.06, 'High': 58249.98, 'Low': 57706.83, 'Close': 58020.51, 'Volume': 1016.56364, 'OpenInterest': 0.0}, 
# {'Time': 1638219600000, 'Open': 58031.13, 'High': 58393.12, 'Low': 57987.83, 'Close': 58249.17, 'Volume': 1128.37772, 'OpenInterest': 0.0}, 
# {'Time': 1638223200000, 'Open': 58247.17, 'High': 58353.01, 'Low': 58021.3, 'Close': 58048.28, 'Volume': 997.23036, 'OpenInterest': 0.0}, 
# {'Time': 1638226800000, 'Open': 58048.28, 'High': 58095.53, 'Low': 57670.42, 'Close': 57776.25, 'Volume': 980.28887, 'OpenInterest': 0.0}, 
# {'Time': 1638230400000, 'Open': 57776.24, 'High': 57962.6, 'Low': 57527.51, 'Close': 57707.38, 'Volume': 1142.35488, 'OpenInterest': 0.0}, 
# {'Time': 1638234000000, 'Open': 57707.38, 'High': 57773.18, 'Low': 57037.66, 'Close': 57270.24, 'Volume': 1835.81805, 'OpenInterest': 0.0}, 
# {'Time': 1638237600000, 'Open': 57260.05, 'High': 57510.01, 'Low': 57230.6, 'Close': 57357.85, 'Volume': 857.13254, 'OpenInterest': 0.0}, 
# {'Time': 1638241200000, 'Open': 57357.84, 'High': 57412.16, 'Low': 56770.37, 'Close': 57092.91, 'Volume': 1320.13745, 'OpenInterest': 0.0}, 
# {'Time': 1638244800000, 'Open': 57092.92, 'High': 57277.32, 'Low': 56983.98, 'Close': 57205.0, 'Volume': 800.63871, 'OpenInterest': 0.0}, 
# {'Time': 1638248400000, 'Open': 57205.0, 'High': 57282.11, 'Low': 56802.77, 'Close': 56836.09, 'Volume': 494.77419, 'OpenInterest': 0.0}]

# MA =  [None, None, None, None, None, None, None, None, 58044.11444444445, 58021.850000000006, 57881.41888888889, 57710.28666666667, 57636.39888888889, 57504.79666666667]

# EMA = [None, None, None, None, None, None, None, None, 58044.11444444445, 57889.33955555556, 57783.04164444445, 57645.01531555556, 57557.012252444445, 57412.82780195556]

# [None, None, None, None, None, None, None, None, 48829.40444444444, 48962.26333333333, 49052.522222222215, 49086.98555555555]
# [None, None, None, None, None, None, None, None, 48829.40444444444, 48868.06555555555, 48905.84644444444, 48960.931155555554]

# [None, None, None, None, None, None, None, None, 49771.194241850826, 49583.848032987735, 49411.52891566372, 49428.853326499055]  MA+2*
# [None, None, None, None, None, None, None, None, 48829.40444444444, 48962.263333333336, 49052.522222222215, 49086.985555555555]  MA
# [None, None, None, None, None, None, None, None, 47887.61464703805, 48340.67863367894, 48693.51552878071, 48745.117784612055] MA-2*

k_list = [
{'Time': 1638633600000, 'Open': 48201.53, 'High': 48477.6, 'Low': 47777.03, 'Close': 47826.98, 'Volume': 2269.94419, 'OpenInterest': 0.0}, 
{'Time': 1638637200000, 'Open': 47847.77, 'High': 48370.51, 'Low': 47787.31, 'Close': 48244.64, 'Volume': 1460.58227, 'OpenInterest': 0.0}, 
{'Time': 1638640800000, 'Open': 48238.47, 'High': 48872.21, 'Low': 48158.03, 'Close': 48871.1, 'Volume': 1821.40053, 'OpenInterest': 0.0}, 
{'Time': 1638644400000, 'Open': 48875.83, 'High': 49444.0, 'Low': 48636.69, 'Close': 49250.0, 'Volume': 2220.94398, 'OpenInterest': 0.0}, 
{'Time': 1638648000000, 'Open': 49250.0, 'High': 49479.99, 'Low': 48958.15, 'Close': 49254.67, 'Volume': 2061.54535, 'OpenInterest': 0.0}, 
{'Time': 1638651600000, 'Open': 49257.51, 'High': 49353.17, 'Low': 48499.81, 'Close': 48694.63, 'Volume': 1507.86582, 'OpenInterest': 0.0}, 
{'Time': 1638655200000, 'Open': 48704.29, 'High': 49285.17, 'Low': 48606.71, 'Close': 49207.85, 'Volume': 1038.1672, 'OpenInterest': 0.0}, 
{'Time': 1638658800000, 'Open': 49207.84, 'High': 49485.97, 'Low': 48830.72, 'Close': 49167.04, 'Volume': 1400.63961, 'OpenInterest': 0.0}, 
{'Time': 1638662400000, 'Open': 49159.14, 'High': 49683.05, 'Low': 48326.32, 'Close': 48947.73, 'Volume': 3066.59031, 'OpenInterest': 0.0}, 
{'Time': 1638666000000, 'Open': 48938.66, 'High': 49235.77, 'Low': 48645.0, 'Close': 49022.71, 'Volume': 1242.54712, 'OpenInterest': 0.0}, 
{'Time': 1638669600000, 'Open': 49030.97, 'High': 49110.99, 'Low': 48797.46, 'Close': 49056.97, 'Volume': 1052.09858, 'OpenInterest': 0.0}, 
{'Time': 1638673200000, 'Open': 49052.69, 'High': 49370.95, 'Low': 48844.17, 'Close': 49181.27, 'Volume': 1174.80203, 'OpenInterest': 0.0}]



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

MA = c_ma(k_list,9,'Close')
print(MA)

# def c_ema(data,ma,interval,price='Close'):
#     EMA = []
#     a = 2/(interval+1)
#     firseEMA = False
#     for i in range(len(ma)):
#         if ma[i]>0:
#             if not firseEMA:
#                 firseEMA = True
#                 EMA.append(ma[i])
#             else:
#                 EMA.append(float('%.3f'% (a*float(data[i][price])+(1-a)*EMA[i-1])))
#         else:
#             EMA.append(ma[i])
#     return EMA

# EMA = c_ema(k_list,MA,9,'Close')
# print(EMA)

def c_bb(data,ma,interval,interval2 = 2,price='Close'):
    stdev = []
    up = []
    down = []
    for i in range(len(ma)):
        if ma[i]>0:
            sum = 0
            for j in range(interval):
                sum+=math.pow((float(data[i-j][price])-ma[i]),2)
            stdev.append(float(math.sqrt(sum/interval)))
        else:
            stdev.append(0.0)
        up.append(float('%.3f'% (ma[i]+interval2*(stdev[i]))))
        down.append(float('%.3f'% (ma[i]-interval2*(stdev[i]))))
    return [up,ma,down]

# stdev = []
# for i in range(len(MA)):
#     if MA[i]>0:
#         sum = 0
#         for j in range(9):
#             sum+=math.pow((float(k_list[i-j]['Close'])-MA[i]),2)
#         stdev.append(float(math.sqrt(sum/9)))
#     else:
#         stdev.append(0)

# print(stdev)

bb = c_bb(k_list,MA,9)
print(bb[0][-1])
print(bb[1][-1])
print(bb[2][-1])



symbol = "ETHBUSD"
k_interval = "1h"  #k线周期 1m 3m 5m 15m 30m 1h 2h 4h 6h 8h 12h 1d 3d 1w 1M
boll_interval = 9 #布林周期
stddev = 2 # 标准差系数
def BOLL(self,price='close'):
    result = self.http_client.get_candlestick_data(symbol=symbol, interval=k_interval, startTime=None, endTime=None, limit=boll_interval)
    k_list = self.tojson(result)
    MA = []
    UP = []
    DOWN = []
    for i in range(len(k_list)):
        total = 0
        for j in range(boll_interval):
            if (i-boll_interval+1) >=0:
                total+=float(k_list[i-j][price])
            else:
                break
        MA.append(float('%.3f'% (total/boll_interval)))
        if MA[i]>0:
            sum = 0
            for k in range(boll_interval):
                sum+=math.pow((float(k_list[i-k][price])-MA[i]),2)
            std = float(math.sqrt(sum/boll_interval))
        else:
            std = 0.0
        UP.append(float('%.3f'% (MA[i]+stddev*std)))
        DOWN.append(float('%.3f'% (MA[i]-stddev*std)))
    return [UP,MA,DOWN]
