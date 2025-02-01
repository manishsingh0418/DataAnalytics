import pandas as pd
data = pd.read_excel("C:/Users/manis/Downloads/FINAL450.xlsx")
print(data)
print(data.duplicated().sum())
print(data["EEID"].duplicated().sum())
print(data.drop_duplicates("EEID"))