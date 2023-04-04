import numpy as np


def myAdd(x, y):
    return x + y


myAdd = np.frompyfunc(myAdd, 2, 1)
print(myAdd([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

# frompyfunc() method takes the following arguments:
#
# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

print(type(np.add))  # check if it's a ufunc

# arithmetic
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
arr3 = np.array([3, 5, 6, 2, 7, 1])
newarrAdd = np.add(arr1, arr2)
print(newarrAdd)

newarrSub = np.subtract(arr2, arr1)
print(newarrSub)

newarrrMul = np.multiply(arr1, arr2)
print(newarrrMul)

newarrDiv = np.divide(arr1, arr2)
print(newarrDiv)

newarrPow=np.power(arr1, arr3)
print(newarrPow)

newarrMod=np.mod(arr2, arr3)
print(newarrMod)

newarrRem = np.remainder(arr2, arr3)
print(newarrRem)

newarrQuoMod=np.divmod(arr2, arr3)
print(newarrQuoMod) #first array represents the quotients, second array represents the remainders


#absolute values
arr= np.array([-1, -2, 1, 2, 3, -4])
newarrAbs= np.absolute(arr)
print(newarrAbs)
