import numpy as np

#A discrete difference means subtracting two successive elements

arr = np.array([10, 15, 25, 5])
newarr=np.diff(arr)
print(newarr)

newArr=np.diff(arr, n=2)  #twice
print(newArr)

