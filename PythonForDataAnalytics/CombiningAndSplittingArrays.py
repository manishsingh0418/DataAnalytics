import numpy as np
# arr1 =np.array([30,40,50])
# arr2=np.array([5,5,3])
# print(np.concatenate([arr1,arr2]))
arr1 =np.array([[30,40],[50,10]])
arr2=np.array([[5,5],[3,3]])
print(np.concatenate([arr1,arr2],axis=1))

print(np.hstack([arr1,arr2])) #horizontal concatenation
print(np.vstack([arr1,arr2])) #vertical concatenation

a=np.array([20,40,30,40,10,20])
b=np.array_split(a,3)
print(b)

a=np.array([[20,40,30],[40,10,20]])
b=np.array_split(a,3)
print(b)