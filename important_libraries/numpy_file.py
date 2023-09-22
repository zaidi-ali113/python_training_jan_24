# Creating an array

import numpy as np

# Create a NumPy array from a Python list
my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)

print(arr)

##########################################################################

#Math operations

# Create two NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Perform element-wise addition
result = arr1 + arr2

print(result)

#############################################################################

# Create a NumPy array
arr = np.array([1, 2, 3])

# Multiply the entire array by a scalar
result = arr * 2

print(result)

##############################################################################
#Random number generation

# Generate an array of random integers between 1 and 10
random_integers = np.random.randint(1, 11, size=5)

# Generate random floating-point numbers
random_floats = np.random.rand(3)

print("Random Integers:", random_integers)
print("Random Floats:", random_floats)




