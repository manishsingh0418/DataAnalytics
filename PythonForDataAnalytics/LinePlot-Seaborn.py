import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# data ={
#     "Days":[1,2,3,4,5],
#     "NOP":[50,40,60,30,44]
# }
# df=pd.DataFrame(data)
# print(df)
# sns.lineplot(data=data, x="Days",y="NOP")
# plt.show()

data=pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
print(data)
sns.lineplot(data=data, x="Year",y="Month Name", hue="Segment", style="Country")
plt.show()