import numpy as np

arr=np.arange(1,13)
print(arr)
print(arr.shape)

#reshape

arr=np.arange(1,13)

new_arr=arr.reshape(3,4)
print(new_arr)
print(new_arr.shape)

arr=np.arange(1,13)
print(arr.reshape(4,3))

#automatic dimension

arr=np.arange(1,13)

arr.reshape(3, -1)
arr.reshape(-1, 2)

#reshape into 3D

arr=np.arange(1,25)

new=arr.reshape(2,3,4)
print(new)

#flatten 

arr=np.array([
    [1,2,3],
    [4,5,6]
])

print(arr.flatten())

a=np.array([[1,2],[3,4]])
b=a.flatten()
b[0]=100
print(a)

#ravel

a=np.array([[1,2],[3,4]])
b=a.ravel()
b[0]=77
print(a)