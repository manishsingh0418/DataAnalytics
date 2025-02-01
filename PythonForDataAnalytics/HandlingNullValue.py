import pandas as pd
data =pd.read_csv("company1.csv")
print(data)
print(data.isnull())
print(data.isnull().sum())
print(data.dropna())
import numpy as np
print(data.replace(np.nan,30000))
data["salary"]=data["salary"].replace(np.nan,30000)
print(data)
print(data["salary"].mean())
print(data.fillna(method="bfill"))#backward fill
print(data.fillna(method="bfill"))#forward fill