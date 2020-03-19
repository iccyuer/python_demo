import pandas as pd

def age_18_to_30(a):
    return a>=18 and a<30 # 18<=a<30

def level_a(s):
    return 85<=s<=100

students=pd.read_excel('./Students.xlsx',index_col='ID')

# 筛选 loc 类似于sql where
students=students.loc[students['Age'].apply(age_18_to_30)].loc[students['Score'].apply(level_a)]

print(students)