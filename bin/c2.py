#127份

buy_points = [
    { "1": 0.001 },
    { "0.99": 0.002 },
    { "0.98": 0.004 },
    { "0.97": 0.008 },
    { "0.95": 0.016 },
    { "0.92": 0.032 },
    { "0.87": 0.064 }
]


amount=0
count=0
for p in buy_points:
    for key in p:
        amount+=float(key)*p[key]
        count+=p[key]
        continue

print(amount/count)

print(buy_points[0])
if buy_points[9]:
    print(2)