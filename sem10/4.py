import numpy as np
arr = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])  
my_list=list()
for i in range(len(arr)):
    if i%2==0:
        for j in range(len(arr)):
            if j%2==1:
                my_list.append(arr[i][j])
a1=np.array(my_list)
a1=a1.reshape(3,2)
a2=arr[::2, 1::2]
print(a1)
print(a2)