import pandas as pd
# data = pd.read_excel("pactice_1.xlsx")
# print(data)
# data["Bonus"]=(data["Salary"]/100)*20
# print(data)

data={"Months":["January","February","March","April"]}
a= pd.DataFrame(data)
print(a)
def extract(value):
    return value[0:3]
a["Short_months"]= a["Months"].str.a[0:3].map(extract)
print(a)