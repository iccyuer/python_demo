import pandas as pd

sales=pd.read_excel('./2020-02-18-2020-03-18-团长销售数据统计_20200318_135547.xlsx', index_col='排名')

print(sales.columns)