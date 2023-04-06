import numpy
import numpy as np

num1=6
num2=9
x=numpy.gcd(num1, num2)
print(x)

arr= numpy.array([20, 8, 32, 36, 16])
y=numpy.gcd.reduce(arr)
print(y)