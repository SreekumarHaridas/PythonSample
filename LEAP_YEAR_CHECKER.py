
# THIS IS A SIMPLE CODE FOR CHECKING WHETHER AN YEAR ENTERED IS LEAP YEAR OR NOT
# IF THE YEAR ENTERED IS DIVISIBLE BY 4 or 400, THEN IT IS A LEAP YEAR
year = int(input("Enter the Year ( e.g. 2016): "))

if (year % 4) == 0:
   if (year % 100) == 0:

       if (year % 400) == 0:

           print("{0} is a leap year since it is divisible by 4 or 400".format(year))
       else:
           print("{0} is not a leap year ".format(year))
   else:
       print("{0} is a leap year since it is divisible by 4 ".format(year))
else:
   print("{0} is not a leap year since it is not divisible by 4 or 400".format(year))