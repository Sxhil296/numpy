import numpy as np

print(np.__version__)

arr = np.array([1, 2, 3, 4, 5]) #using list to create an ndarray
print(arr)
print(type(arr))

arr1 = np.array((2, 4, 6, 8))  #using a tuple to create an ndarray
print(arr1)
print(type(arr1))

#0-D arrays
arrD = np.array(42)
print(arrD)
print(arrD.ndim) #to check the number of dimensions

#1-D arrays
arr1D = np.array([2, 3, 4, 5])
print(arr1D)
print(arr1D.ndim) #to check the number of dimensions

#2-D arrays
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)
print(arr2D.ndim) #to check the number of dimensions

#3-D arrays
arr3D = np.array([[[1,2,3], [4,5,6], [7,8,9]]])
print(arr3D)
print(arr3D.ndim) #to check the number of dimensions


#higher dimensional arrays
arrHD = np.array([1, 2, 3, 4, 5], ndmin=5) #define the number of dimensions by using the ndmin argument
print(arrHD)
print(f'number of dimensions: {arrHD.ndim}')