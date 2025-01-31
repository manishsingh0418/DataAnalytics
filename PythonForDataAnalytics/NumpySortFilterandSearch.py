import numpy as np


#Sort

# # ar=np.array([7,8,4,12,9])
# ar=np.array([[7,8,4,12,9],[2,8,5,1,3]])
# print(np.sort(ar))

#Search
#
# ar=np.array([3,4,1,7,8])
# # s=np.where(ar==4)
# s=np.where(ar%2==0)
# print(s)
#
# ar= np.array([1,2,3,4,5])
# ss=np.searchsorted(ar,5)
# print(ss)

#Filter

ar=np.array([20,30,40,50])
# fa=[True,False,True,False]
# new=ar[fa]
# print(new)\

# fa=ar>35
fa=ar%2==1
new=ar[fa]
print(new)
