a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
s=input().lower()
for kk in s:
    for jj in range(len(a)):
        if a[jj]==kk:
            print(jj+1,end=" ")
                    