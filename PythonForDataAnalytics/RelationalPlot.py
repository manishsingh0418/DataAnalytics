import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
#print(data)
sns.relplot(data=data,x="tip",y="total_bill",hue="sex",kind="line",col="day")
plt.show()