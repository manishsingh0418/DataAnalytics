import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data= pd.read_excel("C:/Users/manis/Downloads/Financial Sample.xlsx")
df=pd.DataFrame(data)
print(df)
plt.scatter(df["Year"],df["Month Name"])
plt.show()