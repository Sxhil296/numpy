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

#a non integer string can not be converted to a integer.


#converting datatypes on existing arrays
arrold=np.array([1,2,3,4,5])
print(arrold.dtype) #int64
arrnew=arrold.astype('i')
print(arrnew.dtype) #int32

arrfloat=np.array([1.1, 2.2, 3.3])
print(arrfloat.dtype) #float64
newarr=arrfloat.astype(int)
print(newarr.dtype) #int64
boolarr=newarr.astype(bool)
print(boolarr.dtype) #bool