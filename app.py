import numpy as np

print(np.__version__)
print(np.__config__.show())

vector = np.zeros(10)
print(vector)


no_of_elements = vector.size
print("--no_of_elements-->", no_of_elements)

memory_of_eachElement = vector.itemsize
print("--memory_of_eachElement-->", memory_of_eachElement)

total_memory = no_of_elements * memory_of_eachElement
print("--total_memory-->", total_memory)

print(np.info(np.add(5, 3)))

vector = np.zeros(10)
print("vector null -->", vector)

vector[4] = 1
print("Changed vector null -->", vector)

vector = np.arange(10, 50, 1)
print("vector with range -->", vector)

vector = np.arange(0, 10)
reverse_vector = vector[::-1]
print("reverse vector -->", reverse_vector)

vector = np.arange(0, 9)
matrix = vector.reshape(3, 3)
print("matrix --->", matrix)

# Find the indexes of the non zero elements from this array: [1,2,0,0,4,0].
# Create the array using the np.array() method.
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indexes = np.nonzero(array)
nonzero_indices_whereClause = np.where(array != 0)
print("Indexes of non zero elements -->", non_zero_indexes[0])
print("Indexes of non zero elements using where clause -->",
      nonzero_indices_whereClause[0])

# The identity matrix(ones in diagonal) is a matrix with ones on the main diagonal and zeros elsewhere.
identity_marix = np.eye(3, dtype=int)
print("Identity matrix -->", identity_marix)


# Create a variable named arr which value should be an array with 3 random values.
arr = np.random.rand(3)
arr_int = np.random.randint(0, 10, 3)
print("Array with 3 random values -->", arr)
print("Array with 3 random integer values -->", arr_int)


# Create a variable named arr whose value should be an array with 10 random values.
# Find the maximum value and print it in the console.
arr = np.random.rand(10)
max_value = np.max(arr)
min_value = np.min(arr)
print("Array with 10 random values -->", arr)
print("Maximum value in the array -->", max_value)
print("Maximum value in the array using np.amax() -->", np.amax(arr))
print("Minimum value in the array -->", min_value) 


# Create a variable named arr whose value should be an array with 10 random values.
# Find the "Mean" value and print it in the console.
arr = np.random.rand(10)
mean_value = np.mean(arr)
print("Array with 10 random values -->", arr)   
print("Mean value in the array -->", mean_value)


# Create a matrix with all its values equal to one (1).
# Add zero (0) to the values that are in the center of the matrix.
# Print the matrix in the console.
matrix = np.ones((5, 5))
print(matrix)


zero_matrix = np.zeros((3, 3))
matrix[1:4, 1:4] = zero_matrix
print("Matrix with ones and zeros in the center -->", matrix)

# Add zero (0) as the border values of a 3 x 3 matrix of ones.
# Print the matrix in the console.

border_matrix = np.zeros((3,3))
inside_matrix =  np.ones((1,1))
border_matrix[1:2,1:2] = inside_matrix

print("Matrix with zeros as border values and ones in the center -->", border_matrix)

#check the values of given expressions and print the results in the console.

a = 0 * np.nan
b = np.nan == np.nan
c =np.inf > np.nan
d = np.nan - np.nan
e = np.nan in set([np.nan])
f = 0.3 == 3 * 0.1
print("a -->", a)     #0.0
print("b -->", b)     #True  
print("c -->", c)     #False
print("d -->", d)     #0.00
print("e -->", e)     #True
print("f -->", f)   #False because of the precision issue in floating point arithmetic.


# #Create a matrix whose values should be all the numbers from 0 to 8, with a dimension of 3 x 3.
# Print the diagonal of the matrix in the console.
matrix = np.arange(9).reshape(3,3)
diagonal = np.diag(matrix)
print("matrix-->",matrix)
print("Diagonal of the matrix -->", diagonal)


# Create an 8 x 8 matrix and fill it with a checkerboard pattern.
# Print the matrix in the console.
matrix = np.ones((8,8),dtype=int)
sub_matrix = np.arange(0,2,1,dtype=int).reshape(1,2)
print("Checkerboard pattern matrix -->", sub_matrix)
for i in range(0,8,2):
    for j in range(0,8,2):
        matrix[i:i+2,j:j+2] = sub_matrix    

print("Checkerboard pattern matrix -->", matrix)
