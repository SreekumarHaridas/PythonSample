# THIS PROGRAM WILL ACCEPT AN INTEGER AS INPUT RETURN THE SUM OF NATURAL NUMBERS UPTO THAT INTEGER
number = int(input("ENTER THE Nth NUMBER: "))
number1=number
if number < 0:
   print("\nPLEASE ENTER A POSITIVE NATURAL NUMBER")
else:
   SUM = 0 # INITIALISE SUM TO ZERO
   # SET THE WHILE LOOP CONDITION AS IT STOPS WHEN number <= 0
   while(number > 0):
       SUM += number
       number -= 1
   print("\nTHE SUM OF NATURAL NUMBERS UPTO ", number1, "IS", SUM)




