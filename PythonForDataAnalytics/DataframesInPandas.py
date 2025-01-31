import pandas as pd

data ={"Name":["John","Peter","Lisa"],
       "Age":[25,28,31],
       "Salary":[300000,45000,25000]}
df =pd.DataFrame(data)
print(df)
# data =pd.read_csv("C:/Users/manis/Downloads/FINAL450.xlsx")
# print(data)

data = pd.read_excel("C:/Users/manis/Downloads/FINAL450.xlsx")
print(data)