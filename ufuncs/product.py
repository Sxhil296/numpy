import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
x=np.prod(arr1)
print(x)
y = np.prod([arr1, arr2])
print(y)

#product over an axis
z=np.prod([arr1, arr2], axis=1)
print(z)

#commulative product
a=np.cumprod(arr1)
print(a)