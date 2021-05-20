# THIS PROGRAM WILL ACCEPT TWO SETS OF INTEGERS AND PERFORM SOME SET OPERATIONS
from run import *
# ENTER SET 1
set1 = set()
# ENTERING ELEMENTS TO SET 1
n = int(input("\nENTER NUMBER OF ELEMENTS IN YOUR FIRST SET: "))
print("\nENTER {} INTEGERS AS ELEMENTS OF YOUR FIRST SET BY PRESSING 'ENTER' AFTER EACH ENTRY".format(n))

# ITERATING TILL THE RANGE
for i in range(1, n+1):
    ele = int(input())
    set1.add(ele)  # ADDING ELEMENTS
print("\nTHE ENTERED FIRST SET  IS :\n")
print(set1)

# ENTER SET 2
set2 = set()
# ENTERING ELEMENTS TO SET 2
n2 = int(input("\nENTER NUMBER OF ELEMENTS IN YOUR SECOND SET: "))
print("\nENTER {} INTEGERS AS ELEMENTS OF YOUR SECOND SET BY PRESSING 'ENTER' AFTER EACH ENTRY".format(n2))

# ITERATING TILL THE RANGE
for ii in range(1, n2+1):
    ele2 = int(input())
    set2.add(ele2)  # ADDING ELEMENTS
print("\nTHE ENTERED SECOND SET IS:\n")
print(set2)
while True:
    # TAKE INPUT FROM USER
    choice = input("\nWHICH SET OPERATION YOU ANT TO PERFORM, ENTER YOUR CHOICE (1.UNION/ 2.INTERSECTION/ 3. DIFFERENCE/ 4. SYMMETRIC DIFFERENCE/ 5. PERFORM ALL ): ")

    # CHECKING THE CHOICE USING IF ELSE CONDITIONAL STATEMENTS AND PERFORM THE REQUESTED ACTION
    if choice in ('1', '2', '3', '4', '5'):
        if choice == '1':
            print("\nUNION OF TWO SETS", set1 | set2)
        elif choice == '2':
            print("\nINTERSECTION OF TWO SETS", set1 & set2)
        elif choice == '3':
            print("\nDIFFERENCE OF TWO SETS", set1 - set2)  # ALL ELEMENTS THAT ARE ONLY IN FIRST SET AND NOT IN SECOND SET
        elif choice == '4':
            print("\nSYMMETRIC DIFFERENCE OF TWO SETS", set1 ^ set2) # ALL THE ELEMENTS THAT ARE EITHER IN FIRST SET  OR IN SECOND SET BUT NOT IN BOTH
        elif choice == '5':
            print("\nUNION OF TWO SETS", set1 | set2)
            print("\nINTERSECTION OF TWO SETS", set1 & set2)
            print("\nDIFFERENCE OF TWO SETS", set1 - set2)
            print("\nSYMMETRIC DIFFERENCE OF TWO SETS", set1 ^ set2)

        break
    else:
        print("\nTHE ENTERED OPTION IS INVALID, PLEASE SELECT A VALID OPTION: \n 1.ADDITION/ 2.SUBTRACTION/ 3. MULTIPLICATION/ 4. DIVISION / 5. PERFORM AL: \n ")

run("SET_OPERATIONS.py")  #TO RUN THE PYTHON PROGRAM "SET_OPERATIONS.py" AGAIN BY IMPORTING A FUNCTION "run.py"