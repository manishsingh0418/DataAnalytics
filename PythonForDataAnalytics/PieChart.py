import matplotlib.pyplot as plt
# brands=["Oneplus","Apple","Samsung","Nokia","Redmi"]
# x=[22,35,30,3,10]
# c=["red","silver","blue","pink","orange"]
# plt.pie(x,labels=brands,colors=c)
# plt.show()

import pandas as pd

# Read the Excel file
file_path = "C:/Users/manis/Downloads/Financial Sample.xlsx"
data = pd.read_excel(file_path)

# Convert to DataFrame
df = pd.DataFrame(data)

# Group by 'Year' and sum 'Units Sold'
grouped_by = df.groupby("Year")["Units Sold"].sum()

# Print grouped data
print(grouped_by)

# Plot pie chart with proper values
plt.pie(grouped_by, labels=grouped_by.index, autopct="%.2f%%")
plt.title("Units Sold Per Year")
plt.show()