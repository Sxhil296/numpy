import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

# accessing the elements
# ndarrays are zero indexed

# access 1D arrays
print(arr[1])

print(arr[2] + arr[3])  # adding two elements using their index

# access 2D arrays
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)
print(arr2D[0, 1])  # prints second element of first row

# access 3D arrays
arr3D = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr3D)
print(arr3D.ndim)
print(arr3D[0, 1, 2])


arr3dd = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3dd)
print(f'The third element of the second array of the first array is {arr3dd[0, 1, 2]}.')