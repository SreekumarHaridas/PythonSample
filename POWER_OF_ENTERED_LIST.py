# THIS PROGRAM WILL ACCEPT LIST OF INTEGERS AS INPUT AND PROVIDE ITS n th POWER AS OUTPUT
import matplotlib.pyplot as plt
list1 = []
powerlist=[]
# number of elements in the list as input
n = int(input("Enter number of elements in your list: "))
print("Enter {} integers as elements of your list by pressing 'enter' after each entry".format(n))

# iterating till the range
for i in range(0, n):
    ele = int(input())

    list1.append(ele)  # adding the element
print("The entered list is :")
print(list1)

n2=float(input("Enter the power that you want to find: "))

for ii in list1:
    powers = ii ** n2
    powerlist.append(powers)
# squared_numbers = [number ** % n2 for number in list1]
# print("The {} th power of the entered list is :".format(n2))
print(powerlist)

plt.plot(list1, powerlist, label='{} Power'.format(n2))
plt.xlabel("Integers")
plt.ylabel("{} Power".format(n2))
# Add a legend
plt.legend()

# Show the plot
plt.show()