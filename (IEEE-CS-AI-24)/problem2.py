day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

day += 1
if day > 28 and month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day > 29:
            day = 1
            month += 1
    else:
        day = 1
        month += 1
elif day > 30 and (month == 4 or month == 6 or month == 9 or month == 11):
    day = 1
    month += 1
elif day > 31:
    if month == 12:
        day = 1
        month = 1
        year += 1
    else:
        day = 1
        month += 1

print("Tomorrow's date:")
print("Day:", day)
print("Month:", month)
print("Year:", year)
