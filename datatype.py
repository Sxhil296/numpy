import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)  # check the datatype

arrs = np.array(['abcd', 'efgh', 'ijkl'])
print(arrs.dtype)



#arrays with defined datatype
arr1 = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr1)
print(arr1.dtype)


arr4=np.array([1,2,3,4], dtype='i4')
print(arr4)
print(arr4.dtype)