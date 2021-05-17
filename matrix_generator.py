# THIS PROGRAM WILL ACCEPT ARRAY OF INTEGERS AS INPUT AND LIST ALL ELEMENTS THAT ARE DIVISIBLE BY THE ENTERED INTEGER
import numpy as np
def matrix_generator(matrix_number):
    matrix = {}
    for ii in range(1, matrix_number + 1):
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
        for i in range(len(array1)):
            x = float(input())
            array1[i] = x
        array121 = np.floor(array1)
        array12 = array121.astype(
            int)  # THE ENTERED ARRAY ELEMENTS ARE ACTUALLY FLOAT VALUES HERE WE CONVERT IT TO INTEGERS
        matrix[ii] = array12.reshape(rows, columns)
    return matrix




