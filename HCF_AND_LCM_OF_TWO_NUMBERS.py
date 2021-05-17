# THIS PYTHON PROGRAM UTILISING THE "hcf_calculator" and lcm_calculator FUNCTION TO FIND THE H.C.F AND L.C.M OF TWO ENTERED INTEGERS
from hcf_calculator import *
from lcm_calculator import *

num1 = int(input("ENTER THE FIRST NUMBER: "))
num2 = int(input("ENTER THE SECOND NUMBER: "))
SELECT = input("WHICH ONE DO YOU WANT TO FIND: H.C.F (enter H) OR L.C.M (enter L)  OR BOTH (enter B): ")

if SELECT == 'H' or SELECT == 'h':
    HCF = hcf_calculator(num1, num2)
    print("\nTHE H.C.F. IS : ", HCF)
elif SELECT == 'L' or SELECT == 'l':
    LCM = lcm_calculator(num1, num2)
    print("\nTHE L.C.M IS : ", LCM)
elif SELECT == 'B' or SELECT == 'b':
    HCF = hcf_calculator(num1, num2)
    print("\nYOU OPTED FOR THE CALCULATION OF BOTH H.C.F AND L.C.M")
    print("\nTHE H.C.F. IS : ", HCF)

    LCM = lcm_calculator(num1, num2)
    print("\nTHE L.C.M IS : ", LCM)

    PRODUCT1 = num1 * num2
    PRODUCT2 = HCF * LCM
    print("\nTHE PRODUCT OF ENTERED NUMBERS IS: ", PRODUCT1)
    print("\nTHE PRODUCT OF HCF AND LCM OF ENTERED NUMBERS IS: ", PRODUCT2)
else:
    print("\nTHE ENTERED OPTION IS INVALID, PLEASE SELECT A VALID OPTION: \n FOR H.C.F (enter H): FOR L.C.M (enter L): FOR BOTH (enter B): ")
