# PYTHON CODE TO FIND THE LARGEST AMONG THREE USER INPUT NUMBERS

number1 = float(input("ENTER THE FIRST NUMBER : "))
number2 = float(input("ENTER THE SECOND NUMBER : "))
number3 = float(input("ENTER THE THIRD NUMBER : "))

if (number1 >= number2) and (number1 >= number3):
   LARGEST_NUMBER = number1
   ENTRY_POSITION = "FIRST"
elif (number2 >= number1) and (number2 >= number3):
   LARGEST_NUMBER = number2
   ENTRY_POSITION = "SECOND"
else:
   LARGEST_NUMBER = number3
   ENTRY_POSITION = "THIRD"

print("THE LARGEST NUMBER IS {} AND IS THE '{}' ENTRY".format(LARGEST_NUMBER, ENTRY_POSITION))