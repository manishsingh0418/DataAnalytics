import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=sns.load_dataset("tips")
print(data)
sns.boxplot(data=data, x="tip", y="sex" , orient="horizontal")
plt.show()