# universal functions
# used to implement vectorisation
# provide broadcasting, reduce, accumulate, etc
# take additional arguments like where dtype out
# Converting iterative statements into a vector based operation is called vectorization.
import numpy as np

# It is faster as modern CPUs are optimized for such operations.


x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
# without numpy's ufunc
z = []
for i, j in zip(x, y):
    z.append(i + j)
print(z)

# with numpy's unfunc
a = np.add(x, y)
print(a)
