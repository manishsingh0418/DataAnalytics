import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# data=sns.load_dataset("tips")
# print(data)
# sns.violinplot(data=data,x="total_bill")
# plt.show()


df =pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
sns.violinplot(data=df,x="Year")
plt.show()