import numpy as np
arr = np.array([[34,43,73],[82,22,12],[53,94,66]]) 
print(arr[arr[:,1].argsort()])