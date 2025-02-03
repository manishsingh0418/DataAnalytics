import pandas as pd

data = pd.read_excel("ESD.xlsx")
print(data.head(10))
# gp = data.groupby("Department").agg({"Gender":"count"})
gp = data.groupby("Department","Gender").agg({"EEID":"count"})
print(gp)
# gp1 = data.groupby("Country").agg({"Age":"mean"})
gp1 = data.groupby("Country","Gender").agg({"Annual": "max","Age":"min"})
print(gp1)