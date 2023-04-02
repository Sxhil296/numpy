# splitting is reverse of joining - breaks one array into multiple

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
newArr = np.array_split(arr, 3)
print(newArr)
print(newArr[0])
print(newArr[1])
print(newArr[2])

# splitting 2D arrays
array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
newArray = np.array_split(array, 2)
print(newArray)
print(newArray[0])
print(newArray[1])

#use axis=1 or hsplit() to split along rows
newArrRow=np.hsplit(array, 2)
print(newArrRow)
newArrayRows=np.array_split(arr, 2, axis=1)
print(newArrayRows)

#you can use vsplit() and dsplit() also