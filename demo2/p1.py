import pandas as pd
import os
import sys

# 读取某一文件下的excel文件,加一个文件夹层级保持原excel文件名
excel_name=os.listdir(sys.argv[1])[0]

# 读取excel文件(B:V列)
sales=pd.read_excel('./'+ sys.argv[1] + '/' + excel_name,usecols = 'B:V')

# 以销售额降序、排名升序  排序
sales.sort_values(by=['销售额','排名'],inplace=True,ascending=[False,True])

# 留存前30条数据
sales=sales.head(30)

# 区list
areas=[]

# for店铺地址列，找出区
for i in sales['店铺地址']:
    if type(i)==str and len(i)>0:
        try:
            areas.append(i[i.rindex('市')+1:i.rindex('区')+1])
        except ValueError:
            areas.append('')
    else:
        areas.append('')

# DataFrame添加区列
sales['地区']=areas

# 设置排名为索引列
sales.set_index('排名',inplace=True)

# 输出excel文件
sales.to_excel('./' + sys.argv[1] + '/' + 'output_' + excel_name)

print('Done!')