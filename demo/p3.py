import pandas as pd

# 行和列 用Series数据结构表示,把Series加入到DataFrame形成行和列
# DataFrame的一列/行就是一个Series

d={'x':100,'y':200,'z':300}
print(d.keys()) # dict_keys(['x', 'y', 'z']) 

s1=pd.Series(d) # 方式1
print(s1.index) # Index(['x', 'y', 'z'], dtype='object') Series的索引值


s2=pd.Series([100,200,300],index=['x','y','z']) # 方式2
print(s2.index)

ss1=pd.Series([1,2,3],index=[1,2,3],name="A")
ss2=pd.Series([10,20,30],index=[1,2,3],name="B")
ss3=pd.Series([100,200,300],index=[1,2,3],name="C")

# Series中的index和DataFrame中的索引列的关系：对齐关系
# 找到相同的index值对成一行


# 以dict方式添加 把ss123当做列加入到DataFrame
df=pd.DataFrame({ss1.name:ss1,ss2.name:ss2,ss3.name:ss3})
print(df)
# df.to_excel('hehe.xlsx')

# 以list方式添加 把ss123当做行加入到DataFrame
df2=pd.DataFrame([ss1,ss2,ss3])
print(df2)