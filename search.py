import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
x=np.where(arr == 4) #returns the index value of 4
print(x)


array=np.array([1,2,3,4,2,5,6,7,2,6,2])
y=np.where(array == 2)
print(y)


#find the indexes where the values are even
z=np.where(arr%2 == 0)
print(z)

#find the indexes where the values are odd
a=np.where(arr%2==1)
print(a)

#searchSorted() - performs binary search in the array, assumed to be used on sorted arrays
arrays=np.array([6,7,8,9])
i = np.searchsorted(arrays, 7)
print(i)

arrs= np.array([3,5,2,1])
e=np.searchsorted(arrs, 2)
print(e) #gives wrong value cause the array is not sorted

#search from the right side
item = np.searchsorted(arrays, 7, side='right')
print(item)

#multiple values
items=np.searchsorted(arrays, [7,8, 9])
print(items)