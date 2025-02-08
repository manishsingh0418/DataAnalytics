import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data=sns.load_dataset("tips")
print(data)
gp=data.groupby("day").agg({"tip":"mean"})
sns.heatmap(gp)

plt.show()