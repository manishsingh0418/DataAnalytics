import matplotlib.pyplot as plt
# l=[1,3,4,7,12,2,8,9,24]
# l1=[2,3,4,6,3,5,7,3,6]
# plot_values=[l,l1]
# plt.boxplot(plot_values)
# plt.show()
import pandas as pd

# Read the Excel file
file_path = "C:/Users/manis/Downloads/Financial Sample.xlsx"
data = pd.read_excel(file_path)

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)
plt.boxplot(df["Year"])

plt.show()