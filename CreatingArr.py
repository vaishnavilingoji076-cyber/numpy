import numpy as np

arr=np.array([10,20,30,40])
print(arr)
print(type(arr))

#2d array
arr=np.array([
    [1,2,3],
    [4,5,6]
])

print(arr)

#3d array
arr=np.array([
    [
        [1,2],
        [3,4]
    ],
    [
        [5,6],
        [7,8]
    ]
])

print(arr)

#shape
arr=np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.shape)
print(arr.ndim)

a=np.array([1,2,3])
print(a.ndim)

print(arr.size)
print(a.size)

print(arr.dtype)
print(a.dtype)

#changing data types
arr=np.array([1,2,3],dtype=float)
print(arr)
print(arr.dtype)