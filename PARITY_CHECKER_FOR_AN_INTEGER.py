
# Code to check if the input integer number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

number = int(input("Enter the Integer Number: "))
remainder = number % 2
if remainder == 0:
   print("{0} is an Even Number".format(number))
else:
   print("{0} is an Odd Number".format(number))