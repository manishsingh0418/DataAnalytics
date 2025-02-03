import pandas as pd
data1 = {"Emp Id":["E01","E02","E03","E04","E05","E06"],
         "Name":["Ram","Shyam","Rahul","Vishal","Ravi","John"],
         "Age":[34,56,23,44,32,36]}
data2= {"Emp Id":["E01","E02","E03","E04","E05","E06"],
         "Salary":[45000,56000,34000,30000,50000,62000]}

df1= pd.DataFrame(data1)
df2= pd.DataFrame(data2)
# print(df1)
# print()
# print(df2)
# print(pd.merge(df1,df2,on="Emp Id", how="left"))
print(pd.concat([df1,df2]))