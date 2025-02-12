import seaborn as sns
import matplotlib.pyplot as plt
data = sns.load_dataset("tips")
sns.kdeplot(data=data,x="total_bill", hue="day ")
plt.show()