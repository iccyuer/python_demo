import pandas as pd
from datetime import date,timedelta

# skiprows跳过几行,usecols读取哪些列'C,D,E,F,G',dtype:设置读取类型(如果设置int,一旦有空数据,NaN转换时就会出错)
bookes=pd.read_excel('./Books.xlsx',skiprows=4,usecols='C:I',dtype={'ID':str,'InStore':str,'Date':str})
# print(bookes['ID'])
# bookes['ID'].at[0]=100
# print(bookes['ID'])
print(type(bookes)) # <class 'pandas.core.frame.DataFrame'> DataFrame
print(type(bookes['ID'])) # <class 'pandas.core.series.Series'> Series
# bookes['ID'].at[i]  通过Series修改值
# bookes.at[i,'ID']  通过DataFrame修改值

# pandas 读取excel文件时，当这一列出现NaN时，会自动把这一列的数据类型设置成Float类型

def add_month(d,md):
    yd=md // 12
    m=d.month + md % 12
    if m!=12:
        yd+=m // 12
        m=m%12
    return date(d.year+yd,m,d.day)

start= date(2020,3,18)
for i in bookes.index:
    bookes['ID'].at[i]=i+1
    bookes['InStore'].at[i]= 'Yes' if i%2==0 else 'No'
    # bookes['Date'].at[i]=start+timedelta(days=i) # 每次+1天
    # bookes['Date'].at[i]=date(start.year+i,start.month,start.day) # 每次+1年
    bookes['Date'].at[i]=add_month(start,i) # 每次+1月

print(bookes)
