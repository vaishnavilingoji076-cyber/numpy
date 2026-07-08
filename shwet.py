import numpy as np

a=np.array([1,2,3,4])
print(a)

arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr)


arr=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr)

arr=np.array([[1,2,3],[4,5,6]])
print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)


print(np.zeros((2,3)))
print(np.ones((2,2)))
print(np.full(2,2),5)
print(np.arange(1,10))
print(np.linspace(0,10,5))

arr=np.array([10,20,30,40])
print(arr[0])

arr=np.array([1,2,3,4,5])
print(arr[1:4])

a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b)
print(a-b)
print(a*b)
print(a/b)