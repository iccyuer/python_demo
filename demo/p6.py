import pandas as pd
pd.DataFrame

products=pd.read_excel('./List.xlsx',index_col='ID')
# ascending默认True 升序  如果两次sort_values排序第二次会把第一次排序
# products.sort_values(by='Worthy',inplace=True,ascending=False)
# products.sort_values(by='Price',inplace=True,ascending=False)

# 如果需要两个排序规则,需要写到一个sort_values中
products.sort_values(by=['Worthy','Price'],inplace=True,ascending=[True,False])
print(products)