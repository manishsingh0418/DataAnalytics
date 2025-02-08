import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("tips") #loading data from github
print(data)
sns.barplot(data=data,x='day', y='tip',estimator='median',hue="sex", palette="GnBu",order=["Sun","Sat","Fri","Thurs"],errorbar=("ci",0))
plt.show()