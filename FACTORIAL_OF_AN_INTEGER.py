# THIS PROGRAM WILL ACCEPT AN INTEGERS AS INPUT AND RETURN ITS FACTORIAL AS RESULT
import numpy as np
NUMBER = int(input("ENTER A POSITIVE INTEGER (e.g. 5): "))
FACTORIAL = 1

# IF ELSE CONDITIONAL STATEMENTS ARE USED HERE TO CHECK WHETHER THE ENTERED INTEGER IS POSITIVE, ZERO, OR NEGATIVE
if NUMBER < 0:
   print("\nYOU ENTERED A NEGATIVE INTEGER, FACTORIAL DOESN'T EXISTS FOR NEGATIVE NUMBERS")
elif NUMBER == 0:
   print("\nTHE FACTORIAL OF 0 IS 1")
else:
   for i in range(1,NUMBER + 1):
       FACTORIAL = FACTORIAL*i
   print("\nTHE FACTORIAL OF", NUMBER, "IS", FACTORIAL)



