import numpy as np
arr = np.array([(11, 22, 33) ,(44, 55, 66), (77, 88, 99)])
l=list()
for i in arr:
    for x in range(len(arr)):
        if x==1:
            l.append(i[x])
ar= np.array(l)          
print(ar)