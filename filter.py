# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# A boolean index list is a list of booleans corresponding to indexes in the array.

import numpy as np

array = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newArr = array[x]
print(newArr)

# creating a filter array
arr = np.array([31, 32, 33, 34])
# create an empty list
filter_arr = []

# iterate
for element in arr:
    if element > 32:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newArray = arr[filter_arr]
print(filter_arr)
print(newArray)


# import numpy as np
# arr = np.array([41, 42, 43, 44])
# filter_arr = arr > 42
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)
