import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[45,67,33,67,12]
y1=[41,60,13,66,13]
y2=[11,30,55,60,19]
y3=[11,40,45,90,59]
plt.figure(figsize=[5 ,3])
plt.plot(x,y,label="male")
plt.plot(x,y1, label="female")
plt.plot(x,y2,label="kids")
plt.legend(loc=1)
plt.legend(["a1","a2","a3"],ncols=3)
plt.legend(bbox_to_anchor=(0.8,1.2),ncols=3,labelspacing=2)
plt.show()