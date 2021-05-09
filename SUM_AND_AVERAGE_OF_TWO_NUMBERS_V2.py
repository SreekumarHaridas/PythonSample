# This program will give you the sum or average of two numbers

num1 = float(input("ENTER THE FIRST NUMBER: "))
num2 = float(input("ENTER THE SECOND NUMBER: "))
SELECT = input("WHICH ONE DO YOU WANT TO FIND: SUM (enter S) OR AVERAGE (enter A) : ")

# Add the entered numbers and display the sum if it is opted to find sum
if SELECT == 'S' or SELECT == 's':
    sum = num1 + num2
    X = 'The sum of {} and {} is {}'.format(num1, num2, sum)
    print(X)
# Find average of the entered numbers if opted so
elif SELECT == 'A' or SELECT == 'a':
    sum = num1 + num2
    AVG = sum/2
    Y = 'The average of {} and {} is {}'.format(num1, num2, AVG)
    print(Y)
else:
    print ("The entered option is invalid please select a valid option")




