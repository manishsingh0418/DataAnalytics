import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
# data=sns.load_dataset("tips")
# print(data)
# sns.countplot(data=data,x="day")
# plt.show()

df=pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
print(df)
sns.countplot(data=df,x="Segment")
plt.show()