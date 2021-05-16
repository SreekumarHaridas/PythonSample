# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND PROVIDE ITS MAXIMUM AND MINIMUM VALUES
import numpy as np
# number of elements in the list as input
n = int(input("ENTER NUMBER OF ELEMENTS OF YOUR ARRAY: "))
print("ENTER {} INTEGERS AS ELEMENTS OF YOUR ARRAY BY PRESSING 'ENTER' AFTER EACH ENTRY".format(n))
array1 = np.empty(n)
for i in range(len(array1)):
    x = float(input())
    array1[i] = x
array12 = np.floor(array1)
print("THE ENTERED ARRAY IS  :")
print(array12)
maxElement = np.amax(array12)
maxindux = np.where(array12 == maxElement)
print("\nTHE MAXIMUM VALUE ELEMENT IN YOUR ARRAY IS {} AND IS AT THE POSITION {} :".format(maxElement, maxindux))
minElement = np.amin(array12)
minindux = np.where(array12 == minElement)
print("\nTHE MINIMUM VALUE ELEMENT IN YOUR ARRAY IS {} AND IS AT THE POSITION {} :".format(minElement, minindux))

