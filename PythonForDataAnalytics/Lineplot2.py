import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df = pd.DataFrame(data)
grouped_by=df.groupby("Month Name")["Year"].sum()
print(grouped_by)
plt.plot(grouped_by.index, grouped_by.values)
# plt.plot(df["Month Name"],df["Year"])
print(df)
plt.show()
