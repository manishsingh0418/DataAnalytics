import pandas as pd
df = pd.read_excel("ESD.xlsx")
print(df)
df.loc[(df["Bonus %"]==0),"GetBonus"]="no bonus"
df.loc[(df["Bonus %"]>0),"GetBonus"]="bonus"
print(df.head(10))
data= pd.read_excel("practice_1.xlsx")
print(data)
data["Full Name"]=data["First Name"].str.capitalize() + " "+ data["Last Name"].str.capitalize()
print(data)