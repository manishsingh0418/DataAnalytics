import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[45,34,56,23,45]
plt.subplot(1,3,1)
plt.title("Age")
plt.plot(x,y)

x=[5,6,7,8,9]
y=[67,50,66,56,82]
plt.subplot(1,3,2)
plt.title("Age")
plt.plot(x,y)

x=[1,4,7,8,9]
y=[67,50,66,56,82]
plt.subplot(1,3,3)
plt.title("Height")
plt.plot(x,y)
plt.suptitle("employee data")
plt.savefig("SubPlot.png")
plt.show()