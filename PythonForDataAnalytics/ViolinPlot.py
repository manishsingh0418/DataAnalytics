# import matplotlib.pyplot as plt
# a=[20,30,40,50,0,30,40,40,30,30,70,80,70,75,80,82,88,40,20]
# plt.violinplot(a, showmedians=True)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df=pd.DataFrame(data)
print(df)
plt.violinplot(df["Year"],showmedians=True)
plt.show()