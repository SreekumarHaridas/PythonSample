# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND LIST ALL ELEMENTS THAT ARE DIVISIBLE BY THE ENTERED INTEGER
import numpy as np
# number of elements in the list as input
n = int(input("ENTER NUMBER OF ELEMENTS OF YOUR ARRAY: "))
n1 = int(input("\nENTER AN INTEGER USED FOR DIVISION: "))
print("\nENTER {} INTEGERS AS ELEMENTS OF YOUR ARRAY BY PRESSING 'ENTER' AFTER EACH ENTRY".format(n))

array1 = np.empty(n)
for i in range(len(array1)):
    x = float(input())
    array1[i] = x
array121 = np.floor(array1)
array12 = array121.astype(int) # THE ENTERED ARRAY ELEMENTS ARE ACTUALLY FLOAT VALUES HERE WE CONVERT IT TO INTEGERS
print("THE ENTERED ARRAY IS  :\n")
print(array12)
NEW_ARRAY = np.extract(array12 % n1 == 0, array12)   # EXTRACTING ALL ELEMENTS SUB ARRAY FROM THE ENTERED ARRAY THAT ARE DIVISIBLE BY n1
# FLIT = lambda x: (x % 13 == 0)
# NEW_ARRAY = FLIT (array12)
print("THE NEW ARRAY OF ELEMENTS THAT ARE DIVISIBLE BY", n1, "IS : \n", NEW_ARRAY)
# print(NEW_ARRAY)
