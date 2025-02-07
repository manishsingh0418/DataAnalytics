# import matplotlib.pyplot as plt
# x=["day1","day2","day3","day4","day5"]
# y=[30,40,25,30,40]
# plt.step(x,y,where="mid",marker="o")
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("expense1.xlsx")
df=pd.DataFrame(data)
# print(df)
group =df.groupby("Category").agg({"Amount":"sum"})
print(group)
plt.step(group.index,group["Amount"] ,where="mid",marker="o")
plt.show()