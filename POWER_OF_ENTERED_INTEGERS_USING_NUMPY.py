# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND PROVIDE ITS n th POWER AS OUTPUT
import matplotlib.pyplot as plt
import numpy as np
array1 = []
# number of elements in the list as input
n = int(input("Enter number of elements in your array: "))
print("Enter {} integers as elements of your array by pressing 'enter' after each entry".format(n))

# iterating till the range
for i in range(n):
    ele = float(input())

    array1.append(ele) # adding the element
array12 = np.floor(array1)
print("The entered array is :")
print(array12)

n2 = float(input("Enter the power that you want to find: "))
nthPower = np.power(array12, n2)
# for ii in list1:
#     powers = ii ** n2
#     powerlist.append(powers)
# # squared_numbers = [number ** % n2 for number in list1]
print("The {} th power of the entered array is :".format(n2))
print(nthPower)

plt.plot(array12, nthPower, label='{} Power'.format(n2))
plt.xlabel("Integers")
plt.ylabel("{} Power".format(n2))
# Add a legend
plt.legend()

# Show the plot
plt.show()