# import matplotlib.pyplot as plt
# x=[30,40,68,27,47,59,47,88,44,66,66,33,5,2,50,12,17,16]
# plt.hist(x,bins=15)
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df =pd.DataFrame(data)
print(df)
plt.hist(df["Year"],bins=30)
plt.show()