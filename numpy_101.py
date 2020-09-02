import numpy as np

# exercice 1 - version from numpy
print(np.version.version)

# exercice 2 - creating numpy array
# my solution
array_exercice_2 = np.array([0,1,2,3,4,5,6,7,8,9])
print(array_exercice_2)

# full solution
array_exercice_2 = np.arange(10)
print(array_exercice_2)


# exercice 3 - How to create a boolean array?
# Create a 3×3 numpy array of all True’s

# my solution
array_boolean_3x3 = np.full([3,3],True)
print(array_boolean_3x3)

# solution
array_boolean_3x3 = np.full([3,3],True, dtype=bool)
print(array_boolean_3x3)

# Alternate method:
array_boolean_3x3 = np.ones((3,3), dtype=bool)
print(array_boolean_3x3)

# exercice 4 - How to extract items that satisfy a given condition from 1D array?
# Q. Extract all odd numbers from arr

# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])

# my solution - is the solution
arr = np.arange(10)
arr_output = (arr[arr%2 == 1])
print(arr_output)