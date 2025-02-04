import matplotlib.pyplot as plt
y =[98,67,88,95,88]
x=["Part1","Part2","Part3","Part4","Part5"]
color=["red","green","yellow","blue","orange"]
plt.bar(x,y,color=color)
plt.xlabel("Part of harry Potter ",fontsize=17)
plt.ylabel("Popularity ",fontsize=17)
plt.title("Popularity of different parts of Harry Potter",fontsize=17)
plt.show()

