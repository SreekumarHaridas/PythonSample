# THIS IS THE PYTHON PROGRAM FOR A SIMPLE CALCULATOR THAT PERFORM ARITHMETIC OPERATIONS LIKE ADDITION, SUBTRACTION, MULTIPLICATION, AND DIVISION
# OF TWO ENTERED NUMBERS
from run import *
while True:
    # Take input from the user
    choice = input("\nENTER YOUR CHOICE (1.ADDITION/2.SUBTRACTION/3. MULTIPLICATION/4. DIVISION ): ")

    # CHECKING THE CHOICE USING IF ELSE CONDITIONAL STATEMENTS AND PERFORM THE REQUESTED ACTION
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("ENTER THE FIRST NUMBER : "))
        num2 = float(input("ENTER THE SECOND NUMBER : "))

        if choice == '1':
            ADDITION = num1+num2
            print("\n", num1, "+", num2, "=", ADDITION)

        elif choice == '2':
            SUBTRACTION = num1-num2
            print("\n", num1, "-", num2, "=", SUBTRACTION)

        elif choice == '3':
            MULTIPLICATION = num1*num2
            print("\n", num1, "*", num2, "=", MULTIPLICATION)

        elif choice == '4':
            DIVISION = num1/num2
            print("\n", num1, "/", num2, "=", DIVISION)
        break
    else:
        print("\nTHE ENTERED OPTION IS INVALID, PLEASE SELECT A VALID OPTION: \n 1.ADDITION/ 2.SUBTRACTION/ 3. MULTIPLICATION/ 4. DIVISION : \n ")

run("SIMPLE_CALCULATOR.py")  #TO RUN THE PYTHON PROGRAM "SIMPLE_CALCULATOR.py" AGAIN BY IMPORTING A FUNCTION "run.py"