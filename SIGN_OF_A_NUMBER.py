#THIS CODE GIVES THE SIGN OF A NUMBER ENTERED
number = float(input("Enter the number: "))
if number > 0:
   print("The entered number is %0.2f, that is positive" % number)
elif number == 0:
   print("You entered zero, that is neutral")
else:
   print("The entered number is %0.2f, that is negative" % number)
