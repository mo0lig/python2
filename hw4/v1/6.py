n=int(input("number of elements in first list:"))
m=int(input("number of elements in second list:"))
l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
print("Elements if first list:")
for i in range(n):
    x=int(input())
    l1.append(x)
    if i%2!=0:
        l3.append(x)
        l4.append(x)
print("Elements if second list:")
for i in range(m):
    x=int(input())
    l2.append(x)
    if i%2==0:
        l3.append(x)
        l5.append(x)
print("First list:",l1)
print("Second list:",l2)
print("Element at odd-index positions from list one",l4)
print("Element at even-index positions from list two",l5)
print("Printing Final third list",l3)