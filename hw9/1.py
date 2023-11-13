print("size of first matrix:")
n=int(input("n:"))
m=int(input("m:"))
print("Elements of first matrix:")
a=list()
b=list()
c=list()
lll=list()
for i in range(n):
    for j in range(m):
        s=int(input(f"{i+1}row,{j+1}col:"))
        lll.append(s)
    a.append(lll)
    lll=[]
    
print("size of second matrix:")
x=int(input("n:"))
y=int(input("m:"))
print("Elements of second matrix:")
for i in range(x):
    for j in range(y):
        s=int(input(f"{i+1} row, {j+1} col:"))
        lll.append(s)
    b.append(lll)
    lll=[]
    
if m==x:
    for i in range(n):
        for j in range(y):
            s=0
            lll.append(s)
        c.append(lll)
        lll=[]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    for i in c:
        print(i)
else:
    print("matrix sizes is different")
    
    
    
# for i in range(n):
#     x=input().split()
#     for j in range(m):
#         lll.append(int(x[j]))
#     a.append(lll)
#     lll=[]
# print("size of second matrix:")
# x=int(input("n:"))
# y=int(input("m:"))
# print("Elements of second matrix:")
# for i in range(n):
#     x=input().split()
#     for j in range(m):
#         lll.append(int(x[j]))
#     b.append(lll)
#     lll=[]