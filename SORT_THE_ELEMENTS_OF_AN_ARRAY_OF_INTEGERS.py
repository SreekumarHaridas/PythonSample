# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND SORT IT ASCENDING OR DESCENDING BASED ON THE CHOICE
import numpy as np
# number of elements in the list as input
n = int(input("ENTER NUMBER OF ELEMENTS OF YOUR ARRAY: "))
SELECT = input("\nWHICH STYLE OF SORTING YOU PREFER  : ASCENDING (enter A) OR DESCENDING (enter D) : ")
print("\nENTER {} INTEGERS AS ELEMENTS OF YOUR ARRAY BY PRESSING 'ENTER' AFTER EACH ENTRY".format(n))
array1 = np.empty(n)
for i in range(len(array1)):
    x = float(input())
    array1[i] = x
array12 = np.floor(array1)
print("THE ENTERED ARRAY IS  :\n")
print(array12)

if SELECT == 'A' or SELECT == 'a':
    sorted_array = np.sort(array12)
    print("\nTHE ENTERED ARRAY SORTED IN ASCENDING ORDER IS :\n")
    print(sorted_array)
elif SELECT == 'D' or SELECT == 'd':
        sorted_array = np.sort(array12)
        reverse_array = sorted_array[::-1]
        print("\nTHE ENTERED ARRAY SORTED IN DESCENDING IS :\n")
        print(reverse_array)
else:
    print("THE ENTERED OPTION IS INVALID, PLEASE ENTER A VALID OPTION ")



