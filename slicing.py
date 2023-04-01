import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)
print(arr[1:5])  # prints elements from index 1 to index 5 (excluding index 5)
print(arr[4:])  # from index 4 to end
print(arr[:4])  # from index 0 to index 4 (doesn't include index 4)
print(arr[-3:-1])

# using the step value
print(arr[1:5:2])
print(arr[::2])

# slicing 2D arrays
arr2d = np.array([[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]])
print(arr2d)
print(arr2d[1, 1:4])
print(arr2d[0:2, 2])
print(arr2d[0:3, 1:4])