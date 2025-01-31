import numpy as np
# a=[30,40,20,40,30]
a=[[30,40,20],[40,30,10]]
arr=np.array(a)
print(arr)
print(arr.shape) #rows,columns
print(len(arr)) #number of nested values
print(np.size(arr)) #number of elements
print(type(arr)) #datatype of variable
print(arr.dtype) #datatype of array
print(arr.astype(float)) #conversion of datatype