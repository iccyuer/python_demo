import pandas as pd

df=pd.DataFrame({'ID':[1,2,3,4,5,6], 'Name':['Tim', 'Victor', 'Nick', 'Tom', 'Richrd', 'Lily']}) # 创建数据帧
df=df.set_index('ID') # 设置索引列为ID,替换系统默认生成的索引index
df.set_index('ID',inplace=True) # 设置索引列时,必须用df=再接收一次，或者设置inplace=True
print(df)
df.to_excel('./p1.xlsx') # 生成xlsx文件
print('Done!')