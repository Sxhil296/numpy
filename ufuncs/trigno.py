import numpy as np

x=np.sin(np.pi/2)
print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
y=np.sin(arr)  #tan cos can also be found
print(y)

#convert degrees into radians
#rad=pi/180 *deg

arrDeg=np.array([30, 45, 60, 90, 180, 270, 360])
rad=np.deg2rad(arrDeg)
print(rad)

#radians to degrees
arrRadian = np.array([np.pi/2, np.pi, np.pi/4, 1.5*np.pi, 2*np.pi])
deg=np.rad2deg((arrRadian))
print(deg)

#finding angles
a=np.arcsin(1.0)
print(a)

b=np.arccos(1/2)
print(b)

#hypotenues
base = 3
perp = 4
h=np.hypot(base, perp)
print(h)