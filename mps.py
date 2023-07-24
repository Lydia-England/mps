#####################################################
### mps.py                                        ###
### Author:        Lydia England                  ###
### Creation Date: 07.21.23                       ###
### Last Modified: 07.24.23                       ###
### Purpose: Take in an nxn matrix T.             ###
###          Take sqrt(T) element-wise.           ###
###          Take the tensor product of resultant ###
###          matrix A with its complex conjugate. ###
#####################################################

import numpy as np
import time
import argparse
from   numpy.linalg   import eig
from   terminaltables import AsciiTable

# define a function to check if a matrix is invertible
def is_invertible(a):
    # return True if matrix is square and full rank; false otherwise.
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]

# define sleep times 
'''
   The program "sleeps" (waits a period of time before continuing) throughout.
   This is so that the outputs are more easily interpreted by human eyes.
   If you want to turn this off, set time_a and time_b to 0.
'''
time_a = 0.5   # shorter sleep time
time_b = 0.75  # longer sleep time

decimal_places = 6  # number of decimal places to include in the A tensor A^T output

# get user input number of rows and columns
'''
    The matrix T must be square, so the number of rows and columns will be the same.
    However, the number of rows and number of columns are defined as separate variables. 
    Thus, if you want to work with non-square matrices, all you need to do is replace the 
    num_cols = num_rows statement with a statement collecting number of columns from the user.
'''
num_rows = int(input("T is an nxn matrix.\nEnter the value for n: "))
num_cols = num_rows

# initialize matrices T and A
T = []
A = []

'''
    Collect the matrix values from the user. 
    The matrix values must be entered row-wise, with values separated by a space. 
    Once the values are entered, press the Enter key to be prompted for the next
    row of values (if applicable).

    The user input goes through the following process. 
    First, it is split into separate objects (based on space separators). 
    It is then cast as datatype 'float'.
    The entire row of user input is put into a numpy array. 
    The numpy array is appended to T (which is just a list of values at this point).
'''
# prompt user for matrix values (row-wise)
print("\nPlease enter matrix values row-wise, with values separated by a space.\n")
time.sleep(time_a)
# iterate through number of rows in the matrix
for n in range(num_rows):
    # prompt user to enter space-separated values for each row of the matrix.
    print("Enter the matrix values for row", str(n+1), ": ")
    temp_row = np.array(input().split(), dtype='float')
    T.append(temp_row)  # append row values to T


# convert T to np array; reshape into square matrix 
T = np.asarray(T).reshape((num_rows,num_cols))

# confirm matrix with user
time.sleep(time_a)
print("\nThe matrix you have entered is: \n", T)
time.sleep(time_a)
if input("Press q to quit. Press any other key to confirm and continue with this matrix.\n") == 'q':
    exit()


if input("Press y to check row/column sums of matrix and optionally normalize to 1. Press any other key to skip this step.\n") == 'y':
    row_sum = np.sum(T, axis=1)  # calculate sum of values in each row.
    for i in range(num_rows):
        # if the values in a row do not add to 1, optionally normalize so that they do.
        if row_sum[i] != 1:
            print("Values in row ", str(i+1), " add to ", row_sum[i], " not 1.")
            time.sleep(time_a)
            print("Would you like to normalize row ", str(i+1), "?")
            time.sleep(time_a)
            # if user types 'y' followed by the enter key, the row will be normalized such that
            # its sum will equal 1. If user types any other key, the row will not be normalized.
            if input("Press y for YES. Press any other key to continue without normalizing.\n") == 'y':
                time.sleep(time_a)
                print("Normalizing row ", str(i+1))
                T[i,:] = T[i,:]/row_sum[i]  # normalize row by dividing each value by sum of values.
                time.sleep(time_a)
                print("Row ", str(i+1), "is now ", str(T[i,:]), "\n")

    time.sleep(time_a)
    col_sum = np.sum(T, axis=0)  # calculate sum of values in each column.
    for j in range(num_cols):
        # if the values in a column do not add to 1, optionally normalize so that they do.
        if col_sum[j] != 1:
            print("Values in column", str(j+1), " add to ", col_sum[j], " not 1.")
            time.sleep(time_a)
            print("Would you like to normalize column", str(j+1), "?")
            time.sleep(time_a)
            # if user types 'y' followed by the enter key, the column will be normalized such that
            # its sum will equal 1. If user types any other key, the column will not be normalized.
            if input("Press y for YES. Press any other key to continue without normalizing.\n") == 'y':
                time.sleep(time_a)
                print("Normalizing column", (j+1))
                T[:,j] = T[:,j]/col_sum[j]  # normalize column by dividing each value by sum of values.
                time.sleep(time_a)
                print("Column ", str(j+1), "is now ", str(T[:,j]), "\n")

    # confirm matrix with user
    time.sleep(time_b)
    print("\nThe matrix T is: \n", T)
    time.sleep(time_a)
    if input("Press q to quit. Press any other key to confirm and continue with this matrix.\n") == 'q':
        exit()
    time.sleep(time_a)


# calculate matrix A (square root of matrix T, element-wise).
# each element in matrix A is the square root of each element in matrix T.
print("\nCalculating matrix A...\n")
A     = np.sqrt(T)      # calculate matrix A
time.sleep(time_b)
print("Matrix A is:\n", A)
time.sleep(time_a)

print("\nCalculating Transpose of matrix A...\n")
At    = A.transpose()   # calculate transpose of A 
time.sleep(time_b)
print("Transpose of matrix A is:\n", At)
time.sleep(time_a)

print("\nTaking tensor (Kronecker) product of A and A^T\n")
E = np.kron(A, At)  # calculate tensor product of A and A transpose
time.sleep(time_b)
print("Result is: \n", np.round(E, decimals=decimal_places))

time.sleep(time_b)

# check if the tensor product of A and A transpose is invertible
if is_invertible(E) == True:
    print("\nMatrix E (tensor product of A and A^T) is an invertible matrix of dimension", E.shape)
else:
    print("\nMatrix E (tensor product of A and A^T) is a non-invertible matrix of dimension", E.shape)

time.sleep(time_b)

# calculate eigenvalues, eigenvectors of matrix E
print("\nCalculating eigenvalues and eigenvectors of matrix E...\n")
evals, evecs = eig(E)
# format eigenvalues, eigenvectors as table
table_data = []
table_data.append(['Eigenvalues', 'Eigenvectors'])
for i in range(len(evals)):
    table_data.append([evals[i], evecs[i]])
table = AsciiTable(table_data)
time.sleep(time_b)
print(table.table)

time.sleep(time_a)

# prompt user to determine if array should be saved to a text file
print("\nWould you like to save this matrix to a text file?\n")
if input("Press y for YES. Press any other key to continue without saving.\n") == 'y':
    np.savetxt('E_matrix.txt', E, fmt='%.4f')



