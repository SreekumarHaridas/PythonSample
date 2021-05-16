

x = float(input('Enter  the First Number: '))
y = float(input('Enter the Second Number: '))

# create a temporary variable and swap the values
temp = x    # keep a copy of x in temp
x = y       # replace initial entered value of x with that of y
y = temp    # put value of temp in y


# print('The value of x after swapping is: {}'.format(x))
# print('The value of y after swapping is: {}'.format(y))
# or
print('The value of x after swapping is: % 0.2f'% x)
print('The value of y after swapping is:  % 0.2f'% y)