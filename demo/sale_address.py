import pandas as pd

# 读取excel文件(B:V列)
sales=pd.read_excel('./2020-02-18-2020-03-18-团长销售数据统计_20200318_135547.xlsx',usecols = 'B:V')

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
sales.to_excel('output.xlsx')

print('Done!')