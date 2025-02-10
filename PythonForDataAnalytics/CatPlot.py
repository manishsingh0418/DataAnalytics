import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=sns.load_dataset("tips")
print(data)
sns.catplot(data=data ,x="day", y="tip", kind="count")
plt.show()