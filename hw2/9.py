month=int(input("Input the month (e.g. [1-12]):"))
day=int(input("Input the day:"))
season=""
list=["January","February","March","April","May","June","July","August","September","October","November","December"]
if 0<=month<2 or month==11:
    season="winter"
elif 2<=month<=4:
    season="spring"
elif 5<=month<=7:
    season="summer"
else:
    season="autumn"
print(list[month-1],day,". Season is",season)