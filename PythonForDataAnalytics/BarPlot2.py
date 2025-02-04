import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df=pd.DataFrame(data)
print(df)
group_by=df.groupby("Product")["Segment"].sum()
# plt.bar(df["Segment"],df["Product"])
plt.bar(group_by.index, group_by.values)
print(group_by)
plt.show()