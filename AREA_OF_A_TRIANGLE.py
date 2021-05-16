# THE FOLLOWING CODE WII CALCULATE THE AREA OF THE TRIANGLE FORMED BY THE THREE SIDES ENTERED
x = float(input('Enter  the length of first side: '))
y = float(input('Enter the length of second side: '))
z = float(input('Enter the length of third side: '))

# calculate the semi-perimeter
s = (x + y + z) / 2

# calculate the area
area = (s*(s-x)*(s-y)*(s-z)) ** 0.5
print('The area of the triangle is %0.2f' % area)