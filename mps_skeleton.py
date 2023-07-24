#####################################################
### mps_skeleton.py                               ###
### Author:        Lydia England                  ###
### Creation Date: 07.21.23                       ###
### Last Modified: 07.24.23                       ###
#####################################################

#########################
###  IMPORT PACKAGES  ###
#########################

import numpy as np
import time
import argparse
from   numpy.linalg   import eig
from   terminaltables import AsciiTable
from   datetime       import datetime



##################################
###  CMD LINE ARGUMENT PARSER  ###
##################################

parser = argparse.ArgumentParser(
        prog='MPS',
        description='Enter a transformation matrix; get E matrix and properties.',
        epilog='Example usage:\npython mps.py -n 4 -o\nto run the program with a 4x4 matrix T and output results to files with default names.'
        )
parser.add_argument('-q', '--quiet', action='store_true',
                    help='Run in quiet mode.')
parser.add_argument('--normalize', choices=['off','all'], default='off',
                    help='Normalize input matrix so that the sum of values in each row and column equals 1.') 
parser.add_argument('-n', '--dimension',      required=True, type=int,
                    help='Dimension n of nxn input transformation matrix T.')
parser.add_argument('-d', '--decimal_places', default=6,       type=int,
                    help='Number of decimal places to use for outputs.')
parser.add_argument('-o', '--output',  action='store_true',
                    help='Save matrix E and its eigenvalues/eigenvectors to files.')
parser.add_argument('--write_matrix', default='E-matrix-'+now+'.csv', type=str,
                    help='Filename to write E matrix output to.')
args = parser.parse_args()


############################
###  DEFINITION SECTION  ###
############################

# define a function to check if a matrix is invertible
def is_invertible(a):
    # return True if matrix is square and full rank; false otherwise.
    return a.shape[0] == a.shape[1] and np.linalg.matrix_rank(a) == a.shape[0]

decimal_places = args.decimal_places  # number of decimal places to include in the A tensor A^T output

'''
    The matrix T must be square, so the number of rows and columns will be the same.
    However, the number of rows and number of columns are defined as separate variables. 
    Thus, if you want to work with non-square matrices, all you need to do is replace the 
    num_cols = num_rows statement with a statement collecting number of columns from the user.
'''

# get number of rows from user input; set number of columns to same.
num_rows = args.dimension
num_cols = num_rows

# initialize matrices T and A
T = []
A = []


############################
###  USER INPUT SECTION  ### 
############################ 
''' Collect the matrix values from the user. 
    The matrix values must be entered row-wise, with values separated by a space. 
    Once the values are entered, press the Enter key to be prompted for the next row of values (if applicable). 

    The user input goes through the following process. 
    First, it is split into separate objects (based on space separators). 
    It is then cast as datatype 'float'.
    The entire row of user input is put into a numpy array. 
    The numpy array is appended to T (which is just a list of values at this point).
'''
# prompt user for matrix values (row-wise)
print("Matrix T has dimensions", num_rows, "by", num_cols)
print("Please enter matrix values row-wise, with values separated by a space.\n")
# iterate through number of rows in the matrix
for n in range(num_rows):
    # prompt user to enter space-separated values for each row of the matrix.
    print("Enter the matrix values for row", str(n+1), ": ")
    temp_row = np.array(input().split(), dtype='float')
    T.append(temp_row)  # append row values to T



###########################
###  EXECUTION SECTION  ###
###########################

# convert T to np array; reshape into square matrix 
T = np.asarray(T).reshape((num_rows,num_cols))

if not args.quiet:
    # confirm matrix with user
    print("\nThe matrix you have entered is: \n", T)
    row_sum = np.sum(T, axis=1)  # calculate sum of values in each row.
    col_sum = np.sum(T, axis=0)  # calculate sum of values in each column.
    print("The sum of values in each row of matrix T is: \n", row_sum)
    print("The sum of values in each column of matrix T is: \n", col_sum)
    if input("Press q to quit. Press any other key to confirm and continue with this matrix.\n") == 'q':
        exit()

if args.normalize == 'all':
    row_sum = np.sum(T, axis=1)  # calculate sum of values in each row.
    for i in range(num_rows):
        # if the values in a row do not add to 1, optionally normalize so that they do.
        if row_sum[i] != 1:
            T[i,:] = T[i,:]/row_sum[i]  # normalize row by dividing each value by sum of values.
    col_sum = np.sum(T, axis=0)  # calculate sum of values in each column.
    for j in range(num_cols):
        # if the values in a column do not add to 1, optionally normalize so that they do.
        if col_sum[j] != 1:
            T[:,j] = T[:,j]/col_sum[j]  # normalize column by dividing each value by sum of values.
    # confirm matrix with user
    print("\nThe matrix T is: \n", T)

# calculate matrix A (square root of matrix T, element-wise).
# each element in matrix A is the square root of each element in matrix T.
if not args.quiet: print("\nCalculating matrix A...\n")
A     = np.sqrt(T)      # calculate matrix A
print("Matrix A is:\n", A)

if not args.quiet: print("\nCalculating Transpose of matrix A...\n")
At    = A.transpose()   # calculate transpose of A 
print("Transpose of matrix A is:\n", At)

if not args.quiet: print("\nTaking tensor (Kronecker) product of A and A^T\n")
E = np.kron(A, At)  # calculate tensor product of A and A transpose
print("Matrix E is: \n", np.round(E, decimals=decimal_places))


# check if the tensor product of A and A transpose is invertible
if is_invertible(E):
    print("\nMatrix E (tensor product of A and A^T) is an invertible matrix of dimension", E.shape)
else:
    print("\nMatrix E (tensor product of A and A^T) is a non-invertible matrix of dimension", E.shape)


# calculate eigenvalues, eigenvectors of matrix E
if args.quiet == None: print("\nCalculating eigenvalues and eigenvectors of matrix E...\n")
evals, evecs = eig(E)
# format eigenvalues, eigenvectors as table
table_data = []
table_data.append(['Eigenvalues', 'Eigenvectors'])
for i in range(len(evals)):
    table_data.append([evals[i], evecs[i]])
table = AsciiTable(table_data)
print(table.table)

# save outputs to files
if args.output:
    np.savetxt(args.write_matrix, E, delimiter=",")
    if not args.quiet: print("Matrix E saved to file: ", args.write_matrix)



