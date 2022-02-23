M1 = [[8, 14, -6], 
           [12,7,4], 
           [-11,3,21]]

#To print the matrix
print(M1)

matrix_length = len(M1)
print(matrix_length)

#To read the last element from each row.
for i in range(matrix_length):
    print(M1[i][-1])

M2 = [[3, 16, -6],
           [9,7,-4], 
           [-1,3,13]]

M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]
matrix_length = len(M3)
print(matrix_length)

# Adding Matrices Using Nested List
#To Add M1 and M2 matrices
for i in range(len(M1)):
    for k in range(len(M2)):
            M3[i][k] = M1[i][k] + M2[i][k]    

#To Print the matrix
print("The sum of Matrix M1 and M2 = ", M3)

# Multiplication of Matrices using Nested List
#To Multiply M1 and M2 matrices
for i in range(len(M1)):
    for k in range(len(M2)):
            M3[i][k] = M1[i][k] * M2[i][k]

#To Print the matrix
print("The multiplication of Matrix M1 and M2 = ", M3)