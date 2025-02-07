# import matplotlib.pyplot as plt
# days = [1,2,3,4,5,6,7]
# NOP1=[5,10,30,20,35,60,80]
# NOP2=[10,60,30,75,80,90,120]
# NOP3=[8,30,50,60,70,90,120]
#
# plt.stackplot(days,NOP1,NOP2,NOP3)
# plt.show()

import matplotlib.pyplot as plt
import pandas as pd
data =pd.read_excel("sampledatafoodinfo.xlsx")
df=pd.DataFrame(data)
#print(df)
grouped = df.groupby(["Category"])["Calories","Protein","Fat"].mean()
plt.stackplot(df["Category"].unique(),grouped["Protein"],grouped["Fat"])
plt.show()