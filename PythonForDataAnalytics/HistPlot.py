# import seaborn as sns
# import matplotlib.pyplot as plt
# data=sns.load_dataset("tips") #loading data from github
# sns.histplot(data,x="day",hue="sex",kde=True)
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
data=sns.load_dataset("titanic") #loading data from github
print(data)
sns.histplot(data=data,x="age",hue="who",kde=True)
plt.show()