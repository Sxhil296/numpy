import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# iterating 2d arrays
a = np.array([[1, 2, 3], [4, 5, 6]])

# to get the arrays in the 2d array
for y in a:
    print(y)

# to get every element in the 2d array
for b in a:
    for c in b:
        print(c)

# iterating 3d array
arr3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# to print 2d array of a 3d array
for item in arr3d:
    print(item)

# to print every array in 3d array
for i in arr3d:
    for j in i:
        print(j)

# to print every element of the 3d array
for k in arr3d:
    for l in k:
        for m in l:
            print(m)


#iterating arrays using nditer()
array=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for z in np.nditer(array):
    print(z)

#enumeration - mentioning the sequence number of elements inside the array
arrays=np.array([[1,2,3,4],[5,6,7,8]])
for idx, id in np.ndenumerate(arrays):
    print(idx, id)