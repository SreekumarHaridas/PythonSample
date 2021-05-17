# THIS PROGRAM WILL PROVIDE THE ADDITION, MULTIPLICATION, AND TRANSPOSE  OF TWO MATRICES ENTERED
import numpy as np
from run import *
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
while True:
    # Take input from the user
    choice = input("\nENTER YOUR CHOICE OF MATRIX OPERATION (1.ADDITION/ 2. MULTIPLICATION/ 3. TRANSPOSE ): ")

    # CHECKING THE CHOICE USING IF ELSE CONDITIONAL STATEMENTS AND PERFORM THE REQUESTED ACTION
    if choice in ('1', '2', '3'):
        if choice == '1':
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
                    print("\nTHE SUM OF THE TWO MATRICES ENTERED IS\n ", result)
                else:
                    print("\nTHE DIMENSION OF THE TWO MATRICES ARE NOT SAME, SO MATRIX ADDITION IS NOT POSSIBLE")
            else:
                print("\nTHE NUMBER OF MATRICES ENTERED IS MORE THAN TWO ")
        elif choice == '2':
            if matrix_number == 2: # PERFORM MULTIPLICATION THE MATRICES IF THE ENTERED MATRICES ARE TWO IN NUMBER
                X = matrix.get(1)
                Y = matrix.get(2)
                rows1 = len(X)  # Height.
                columns1 = len(X[0])  # Width
                rows2 = len(Y)  # Height.
                columns2 = len(Y[0])  # Width
                if columns1 == rows2:
                    result1 = np.empty((rows1, columns2))
                    result = result1.astype(int)
                    for i in range(len(X)):
                        # iterate through columns of Y
                        for j in range(len(Y[0])):
                            # iterate through rows of Y
                            for k in range(len(Y)):
                                result[i][j] += X[i][k] * Y[k][j]
                    print("\nTHE PRODUCT OF THE TWO MATRICES ENTERED IS\n ", result)
                else:
                    print("\nTHE DIMENSIONAL CONDITION IS NOT MATCHING FOR MATRIX MULTIPLICATION")
            else:
                print("\nTHE NUMBER OF MATRICES ENTERED IS MORE THAN TWO ")
        elif choice == '3':
            if matrix_number == 2:
                X = matrix.get(1)
                Y = matrix.get(2)
                rows1 = len(X)  # Height.
                columns1 = len(X[0])  # Width
                rows2 = len(Y)  # Height.
                columns2 = len(Y[0])
                result11 = np.empty((columns1, rows1))
                result1 = result11.astype(int)
                result111 = np.empty((columns2, rows2))
                result2 = result111.astype(int)
                for i in range(len(X)):
                    # iterate through columns
                    for j in range(len(X[0])):
                        result1[j][i] = X[i][j]
                for il in range(len(Y)):
                    # iterate through columns
                    for jl in range(len(Y[0])):
                        result2[jl][il] = Y[il][jl]

                print("\nTHE TRANSPOSE OF THE FIRST MATRIX ENTERED IS\n ", result1)
                print("\nTHE TRANSPOSE OF THE SECOND MATRIX ENTERED IS\n ", result2)
            else:
                print("\nTHE NUMBER OF MATRICES ENTERED IS MORE THAN TWO ")
        break
    else:
        print("\nTHE ENTERED OPTION IS INVALID, PLEASE SELECT A VALID OPTION: \n 1.ADDITION/ 2. MULTIPLICATION/ 3. TRANSPOSE: \n ")
run("MATRIX_ADDITION_MULTIPLICATION_TRANSPOSE.py")  #TO RUN THE PYTHON PROGRAM "MATRIX_ADDITION_MULTIPLICATION_TRANSPOSE.py" AGAIN BY IMPORTING A FUNCTION "run.py"