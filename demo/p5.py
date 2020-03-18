import pandas as pd

def add_2(x):
    return x+2

bookes=pd.read_excel('./Books.xlsx', index_col='ID')
bookes['ListPrice']=bookes['ListPrice']+2
bookes['ListPrice']=bookes['ListPrice'].apply(add_2) # Series的apply函数
bookes['ListPrice']=bookes['ListPrice'].apply(lambda x: x+2) # Series的apply函数结合lambda表达式
# bookes['Price']=bookes['ListPrice']*bookes['Discount'] # 列*列
# bookes['Price']=bookes['ListPrice']*8 # 列*数值

# 同样可以单元格*单元格
for i in bookes.index:
    bookes['Price'].at[i]=bookes['ListPrice'].at[i]*bookes['Discount'].at[i]

# 可以对列进行条件判断计算
for i in range(5,16):
    bookes['Price'].at[i]=bookes['ListPrice'].at[i]*bookes['Discount'].at[i]
print(bookes)