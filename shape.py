import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)
print(a.shape) #returns a tuple with each index having the number of corressponding elements


b=np.array([1,2,3,4,5], ndmin=5)
print(b)
print(b.shape)

#reshaping arrays
c= np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(c)
print(c.shape)
d=c.reshape(4,3)
print(d)
print(d.shape)
e=c.reshape(2,3,2)
print(e)
print(e.shape)
print(e.base) #view

#flattening the arrays
arr=np.array([[1, 2, 3], [4, 5, 6]])
newarr=arr.reshape(-1)
print(newarr)