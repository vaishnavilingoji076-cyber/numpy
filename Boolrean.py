import numpy as np

arr=np.array([10,20,30,40,50])
print(arr>25)

#filtering data
arr=np.array([10,20,30,40,50])
print(arr[arr>25])

#find even numbers
arr=np.array([1,2,3,4,5,6,7,8,])
print(arr[arr %2==0])
print(arr[arr%2!=0])
print(arr[arr==20])
print(arr[arr!=20])

#combining conditions
arr=np.array([10,20,30,40,50])
print(arr[(arr>20) & (arr < 60)])