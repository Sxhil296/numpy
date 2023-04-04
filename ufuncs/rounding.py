# truncation - Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.

import numpy as np

arr = np.trunc([-3.1666, 3.6667])
arrf = np.trunc([-3.1666, 3.6667])
print(arr)
print(arrf)

# rounding
# around() - increments preceding digit or decimal by 1 if >=5 else do nothing
arrA = np.around(3.1666, 2)
print(arrA)

# floor - rounds off decimal to nearest lower integer.
arrFl=np.floor([-3.1666, 3.669])
print(arrFl)

#ceil -  rounds off decimal to nearest upper integer.
arrCl = np.ceil([-3.1666, 3.669])
print(arrCl)
