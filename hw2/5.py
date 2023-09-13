print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")
x=input("Input the name of Month:")
a=False
list=["January","February","March","April","May","June","July","August","September","October","November","December"]
l=["31","28/29","31","30","31","30","31","31","30","31","30","31"]
if x in list:
    for i in range(len(list)):
        if x==list[i]:
            print("No. of days:",l[i] ,"days")
            a=True
            break
if a==False:print("Please, enter the correct month name")