year=int(input("Input your birth year: "))
if (year - 2000) % 12 == 0:
    sign = 'Dragon'
elif (year - 2000) % 12 == 1:
    sign = 'Snake'
elif (year - 2000) % 12 == 2:
    sign = 'Horse'
elif (year - 2000) % 12 == 3:
    sign = 'sheep'
elif (year - 2000) % 12 == 4:
    sign = 'Monkey'
elif (year - 2000) % 12 == 5:
    sign = 'Rooster'
elif (year - 2000) % 12 == 6:
    sign = 'Dog'
elif (year - 2000) % 12 == 7:
    sign = 'Pig'
elif (year - 2000) % 12 == 8:
    sign = 'Rat'
elif (year - 2000) % 12 == 9:
    sign = 'Ox'
elif (year - 2000) % 12 == 10:
    sign = 'Tiger'
else:
    sign = 'Hare'

print("Your Zodiac sign :",sign)
#В этом я тоже не разбираюсь. Поэтому я это тоже скопировал с интернета. Прошу прощения за это. Но задания в целом легкое и понятное.