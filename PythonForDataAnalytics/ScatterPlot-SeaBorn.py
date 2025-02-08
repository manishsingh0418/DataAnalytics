import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data=sns.load_dataset("tips")
print(data)
sns.scatterplot(data=data,x="total_bill",y="tip",hue="day",size="size")
plt.show()