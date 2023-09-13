seq="";    
a="*"
for i in range(0,7):    
    for j in range(1,7):     
        if ((i==0 or i==3) and (j>0 and j<5)) or (j==1) or ((i==1 or i==2) and j==5) or (j+1==i):    
            seq+=a   
        else:      
            seq+=" "   
    seq+="\n" 
print(seq)