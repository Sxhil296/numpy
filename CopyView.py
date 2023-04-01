import numpy as np

# copy is the new array while view is just the view of the original array

# copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
print(arr)
print(x)
arr[0] = 42
print(arr)
y = arr.copy()
print(y)

# view
a = np.array([1, 2, 3, 4, 5])
z = a.view()
a[0] = 23
print(a)
print(z)



#original array doesn't get affected by changes in copy
b = np.array([21, 32, 43, 54, 65])
c=b.copy()
c[0]=10
print(b)
print(c)


#original array gets affected by changes in view
d=np.array([2,4,6,8])
e=d.view()
e[0]=1
print(d)
print(e)



#copies owns the data and views doesn't

f=np.array([3,6,9,12])
g=f.copy()
h=f.view()
#check if array own its data
print(g.base) #none
print(h.base) #original array