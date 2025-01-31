import numpy as np
import statistics as stats
# baked_food = [200,300,150,130,200,280,170,188]
# a=np.array(baked_food)
# print(np.mean(baked_food))
# print(np.median(baked_food))
# print(stats.mode(baked_food))
# print(np.std(baked_food)) #standard deviation
# print(np.var(baked_food))

# -1 represent inversely proportional relationship
# 1 represents proportional relationship
# 0 means no relationship

tobacco_consumption = [30,50,10,30,50,40]
deaths =[100,120,70,100,120,112]
print(np.corrcoef([tobacco_consumption, deaths])) #coffecient of co relation

price =[300,100,350,150,200]
sales =[10,20,7,17,3]
print(np.corrcoef([price,sales]))
