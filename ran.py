from numpy import random

# random integer b/w 0 and 100
x = random.randint(100)
print(x)

# random float
y = random.rand()
print(y)

# random array containing 5 elements b/w 0 and 100
arr = random.randint(100, size=(5))
print(arr)

# 2D array with 3 rows, each row containing 5 random integers from 0 to 100
array = random.randint(100, size=(3, 5))
print(array)

# 1D array containing 4 random floats
arrFloat = random.rand(4)
print(arrFloat)

# 2D array with 3 rows, 5 elements in each row
arrayFloat = random.rand(3, 5)
print(arrayFloat)

# generate a random number from array
a = random.choice([3, 5, 7, 8, 9])
print(a)

b = random.choice([3, 5, 6, 7, 8, 9], size=(3, 5))
print(b)
