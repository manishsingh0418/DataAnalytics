import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data=sns.load_dataset("tips")
print(data)
sns.stripplot(data=data, x="day", y="total_bill", dodge= True , jitter=0.3)
plt.show()