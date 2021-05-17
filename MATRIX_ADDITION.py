# THIS PROGRAM WILL PROVIDE THE ADDITION OF TWO MATRICES ENTERED
import numpy as np
matrix_number = int(input("ENTER NUMBER OF MATRICES YOU WANT TO CREATE  : "))
matrix = {}
for ii in range(1, matrix_number+1):
    # CREATING MATRIX/MATRICES

    print("ENTER NUMBER OF ROWS OF YOUR ", ii, "MATRIX : ")
    rows = int(input())
    print("ENTER NUMBER OF COLUMNS OF YOUR ", ii, "MATRIX : ")
    columns = int(input())
    number_of_elements = rows * columns
    print("\nENTER {} ELEMENTS FOR YOUR MATRIX".format(number_of_elements))
    # matrix1 = np.empty((rows, columns))
    # matrix = matrix1.astype(int)
    array1 = np.empty(number_of_elements)
    for iii in range(len(array1)):
        x = float(input())
        array1[iii] = x
    array121 = np.floor(array1)
    array12 = array121.astype(int)  # THE ENTERED ARRAY ELEMENTS ARE ACTUALLY FLOAT VALUES HERE WE CONVERT IT TO INTEGERS
    matrix[ii] = array12.reshape(rows, columns)
print(matrix)
# FIND SUM OF THE MATRICES IF THE ENTERED MATRICES ARE TWO IN NUMBER
if matrix_number == 2:
    X = matrix.get(1)
    Y = matrix.get(2)
    if X.shape == Y.shape:
        rows1 = len(X)  # Height.
        columns1 = len(X[0])  # Width
        result1 = np.empty((rows1, columns1))
        result = result1.astype(int)

        for i in range(len(X)):
            # iterate through columns
            for j in range(len(X[0])):
                result[i][j] = X[i][j] + Y[i][j]
        print("\nTHE OF THE TWO MATRICES ENTERED IS\n ", result)
    else:
        print("\nTHE DIMENSION OF THE TWO MATRICES ARE NOT SAME, SO MATRIX ADDITION IS NOT POSSIBLE")

else:
    print ("\nTHE NUMBER OF MATRICES ENTERED IS MORE THAN TWO ")