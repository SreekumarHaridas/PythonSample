# THIS IS A SIMPLE PYTHON PROGRAM THAT DISPLAY CALENDAR OF THE ENTERED YEAR AND MONTH
# importing calendar module
import calendar
year = int(input("PLEASE ENTER THE YEAR ( e.g. 2016): "))
month = int(input('PLEASE ENTER THE MONTH(1-12):'))
monthname = {
        1: 'JANUARY',
        2: 'FEBRUARY',
        3: 'MARCH',
        4: 'APRIL',
        5: 'MAY',
        6: 'JUNE',
        7: 'JULY',
        8: 'AUGUST',
        9: 'SEPTEMBER',
        10: 'OCTOBER',
        11: 'NOVEMBER',
        12: 'DECEMBER'
    }
smallmonths = monthname.get(month)
# smallmonths1 = smallmonths.lower() # ALL IN SMALL FONTS
# smallmonths2 = smallmonths.capitalize() # FIRST LETTER CAPS
# print(smallmonths1)
# print(smallmonths2)


print("THE CALENDAR FOR THE MONTH", smallmonths, "OF THE YEAR-", year)
print(calendar.month(year, month))