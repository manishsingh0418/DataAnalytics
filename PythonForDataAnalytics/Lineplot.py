import matplotlib.pyplot as plt
x=["day1","day2","day3","day4","day5"]
y=[300,420,250,230,400]
y1=[500,450,300,250,320]
plt.plot(x,y,marker="o",ls="--",color="red",label="week1")
plt.plot(x,y1,marker="*",ls="-",color="green",label="week2",alpha=0.5)
plt.legend()
plt.show()