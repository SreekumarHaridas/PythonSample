# THIS IS A SIMPLE PYTHON PROGRAM THAT CONVERT THE DATE ENTERED IN TO THE DAY OF THE YEAR
import numpy as np

year = int(input("PLEASE ENTER THE YEAR ( e.g. 2016): "))
month = int(input('PLEASE ENTER THE MONTH(1-12):'))
day = int(input('PLEASE ENTER THE DAY (1-31):'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            leap_day = 1
            print("{0} IS A LEAP YEAR".format(year))

        else:
            leap_day = 0
    else:
        leap_day = 1
        print("{0} IS A LEAP YEAR".format(year))
else:
    leap_day = 0

monthvalues = np.arange(1, month)
if leap_day == 0:
    monthdays = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
elif leap_day == 1:
    monthdays = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

day_of_year = day

for ii in monthvalues:
    day_of_year = day_of_year + monthdays.get(ii)
print("THE DATE {}/{}/{} IS EQUIVALENT TO DAY OF YEAR {} ".format(day, month, year, day_of_year))
