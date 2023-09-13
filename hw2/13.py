a=int(input("Input a year:"))
b=int(input("Input a month [1-12]:"))
c=int(input("Input a day [1-31]:"))
d=0
e=0
list=["January","February","March","April","May","June","July","August","September","October","November","December"]
l=[31,28,31,30,31,30,31,31,30,31,30,31]
if b>12:
    print("The amount of months in one year is max 12. Please, enter again correct number") #Если пользователь введет неправильное число месяца, то программа выводит это как ошибку
elif c>l[b-1]:
    print("In this month your day doesn't exist. Younr month",list[b-1],"is limited by",l[b-1])
else:
    if c+1>l[b-1]: #если введенный день месяца будет равно максимальному количеству дня в том месяце,то добавляет +1 к числу месяца
        d=1
        b+=1
        if b>12: #Это для того, чтобы когда, скажем, с 12-го месяца число изменится на 1, то оно станет следующим годом.
            e=1
            print("The next date is [yyyy-mm-dd]",a+1,"-",e,"-",d) #Это для того, чтобы когда, скажем, с 12-го месяца число изменится на 1, то оно станет следующим годом.
        else:
            print("The next date is [yyyy-mm-dd]",a,"-",b,"-",d) # А это если количество месяцев не превышает 12, то тогда всего лишь месяц изменятеся
    else:
        print("The next date is [yyyy-mm-dd]",a,"-",b,"-",c+1) 
    