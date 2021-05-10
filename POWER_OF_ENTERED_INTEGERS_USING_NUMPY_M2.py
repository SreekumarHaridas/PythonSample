# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND PROVIDE ITS n th POWER AS OUTPUT
import matplotlib.pyplot as plt
import numpy as np
# number of elements in the list as input
n = int(input("Enter number of elements in your array: "))
print("Enter {} integers as elements of your array by pressing 'enter' after each entry".format(n))
array1 = np.empty(n)
for i in range(len(array1)):
    x = float(input())
    array1[i] = x
array12 = np.floor(array1)
print("The entered array is :")
print(array12)

n2 = float(input("Enter the power that you want to find: "))
nthPower = np.power(array12, n2)
print("The {} th power of the entered array is :".format(n2))
print(nthPower)
plt.plot(array12, nthPower, label='{} Power'.format(n2))
plt.xlabel("Integers")
plt.ylabel("{} Power".format(n2))
# Add a legend
plt.legend()
# Show the plot
plt.show()