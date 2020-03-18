import pandas as pd

p2 = pd.read_excel('./p1.xlsx')
print(p2.shape) # (3, 2) -- 3行2列 不包含头部行
print(p2.columns) # Index(['ID', 'Name'], dtype='object') -- 列名
print(p2.head(6)) # 从头部读取，默认5行
print('---------')
print(p2.tail(3)) # 从尾部读取

print('=========')
pp2=pd.read_excel('./p1.xlsx', header=1) # header 指定第几行为列名,默认第0行
print(pp2.columns) # Index(['ID', 'Name'], dtype='object')

print('=========')
pp3=pd.read_excel('./p1.xlsx', header=None) # header 不指定列名
print(pp3.columns) # Int64Index([0, 1], dtype='int64') 系统默认给定0,1,2...
pp3.columns=['id','name'] # 设置列名
print(pp3.columns)
print(pp3.head())
pp3=pp3.set_index('id')
# pp3.to_excel('./p3.xlsx') # 生成xlsx文件
print('Done!')

print('=========')
pp4=pd.read_excel('./p1.xlsx', index_col='ID') # index_col 指定索引列 默认为None
print(pp4)