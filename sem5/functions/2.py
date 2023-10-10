def add_excitement(list):
    li=[]
    for i in list:
        i+='!'
        li.append(i)
    print(li)
def new_list():
    n=int(input())
    list=[]
    for i in range(n): 
        x=input()
        list.append(x)
    return list

list=new_list()
add_excitement(list)
print(new_list())
