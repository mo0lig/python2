nn,sum,avr,n=0,0,0,0
float(n)
a=True
while a==True:
    nn=int(input())
    sum+=nn
    n+=1
    if(nn==0):
        a=False

print("Sum of integers is:",sum)
print("Average:",round((sum/(n-1)),2)) #үтірлен кейін 2 санға жуықтаймыз