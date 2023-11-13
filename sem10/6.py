import numpy as np
arr=np.arange(10,34,1)
arr=arr.reshape(8,3)
print(np.array_split(arr,3))