import pandas as pd

with pd.ExcelFile('./vlookup.xlsx') as xls:
    df1 = pd.read_excel(xls, 'Sheet5', usecols='A:B')
    df2 = pd.read_excel(xls, 'Sheet6', usecols='A:B')

df1.set_index('id')
print(df1)
print(df2)

sort1=df1.sort_values(by='数学')

print(sort1)
pd.DataFrame(df1)

result=df1.merge(df2,how="left")
result=result.set_index('id')
print(result)

# result.to_excel('path_to_file.xlsx', sheet_name='Sheet1')