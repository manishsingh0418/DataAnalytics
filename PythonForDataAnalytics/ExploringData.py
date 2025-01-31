import pandas as pd
data = pd.read_excel("C:/Users/manis/Downloads/FINAL450.xlsx")
print(data)
print(data.head(10))
print(data.tail(10))
print(data.info())
print(data.describe())
print(data.isnull().sum())