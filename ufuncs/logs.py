# NumPy provides functions to perform log at the base 2, e and 10.
from math import log
import numpy as np

arr = np.arange(1, 10)
print(np.log2(arr))

print(np.log10(arr))

print(np.log(arr))


#NumPy does not provide any function to take log at any base,
# so we can use the frompyfunc() function along with inbuilt function math.log()
# with two input parameters and one output parameter:


nplog=np.frompyfunc(log, 2, 1)
print(nplog(100, 15))