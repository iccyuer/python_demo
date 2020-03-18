import pandas as pd



df=pd.read_excel('lemon.xlsx', 'Sheet1', usecols='A:D', nrows = None, header = [1]) #这个会直接默认读取到这个Excel的第一个表单
# print(df)
data=df.head() #默认读取前5行的数据
print("获取到所有的值:\n{0}".format(data)) #格式化输出
print('-----------')
value=df.values #values 不包含表头
print(value)
print('-----------')
# print(df.ix[0].values)
# test_data=[]
# for i in df.index.values:#获取行号的索引，并对其进行遍历：
#     #根据i来获取每一行指定的数据 并利用to_dict转成字典
#     row_data=df.ix[i,['case_id','module','title','http_method','url','data','expected']].to_dict()
#     test_data.append(row_data)
# print("最终获取到的数据是：{0}".format(test_data))