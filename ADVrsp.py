#resize

import numpy as np

arr=np.array([1,2,7,4])
arr.resize((2,3))

print(arr)

arr.resize((2,2))
print(arr)

#expand_dims
arr=np.array([1,2,3])
new=np.expand_dims(arr, axis=0)

print(new)

new=np.expand_dims(arr, axis=1)
print(new)

#squeez
arr=np.array([[[1,2,3]]])
print(arr.shape)

new=np.squeeze(arr)
print(new)
print(new.shape)

#transpose
arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr.T)