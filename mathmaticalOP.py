import numpy as np

a=np.array([10,20,30])
b=np.array([1,2,3])

print(np.add(a,b))
print(a-b)
print(np.multiply(a,b))
print(a/b)

#floor division
a=np.array([11,22,35])
print(a//2)

#power
arr=np.array([2,3,4])
print(arr**2)

#numpy mathematical functions
arr=np.array([1,4,9,16])
print(np.sqrt(arr))

print(np.square(arr))


#absolute value
arr=np.array([-5,4,-9])
print(np.abs(arr))

#logarithm
arr=np.array([1,10,100])
print(np.log10(arr))


#broadcasting begins
arr=np.array([10,20,30])
print(arr+5)
print(arr*10)

#broadcasting between arrays

a=np.array([
    [1,2,3],
    [4,5,6]
])

b=np.array([10,20,30])

print(a+b)