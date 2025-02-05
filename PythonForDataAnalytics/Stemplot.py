# import matplotlib.pyplot as plt
# x=[10,40,20,40,20,40,20,40,60,70,50,40]
# plt.stem(x,linefmt="--")
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df=pd.DataFrame(data)
plt.stem(df["Year"])
plt.show()