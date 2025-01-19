"""
@author: Maherdeep Chhabra
@email: mchhabr5@asu.edu
"""

# Answer to Question 1
import numpy as np

# Create a random sample from a standard normal distribution
random_sample = np.random.randn(5, 3)

# Multiply each element in the array by 100
result_array = random_sample * 100

# Print the initial random sample
print("Random Sample from Standard Normal Distribution:")
print(random_sample)

# Print the resulting array after multiplication
print("\nResulting Array after Multiplying by 100:")
print(result_array)
print()
# Answer to Question 2
import numpy as np

# Create a one-dimensional numpy array from 10 to 20 with steps of 2
one_dimensional_array = np.arange(10, 21, 2)

# Reshape the one-dimensional array into a two-dimensional array of shape 2x3
two_dimensional_array = one_dimensional_array.reshape(2, 3)

# Output the two-dimensional array to the Python console
print("Two-Dimensional Array:")
print(two_dimensional_array)
print()

# Answer to Question 3

import numpy as np

# Create a numpy array of sequential numbers from 0 to 99
sequential_array = np.arange(100)

# Reshape the array to a multidimensional array with a shape of 20x5
multidimensional_array = sequential_array.reshape(20, 5)

# Output the multidimensional array to the Python console
print("Multidimensional Array (20x5):")
print(multidimensional_array)
print()

# Answer to Question 4
import numpy as np

# Create a random sample of 100 numbers from a continuous uniform distribution
array6 = np.random.random_sample(100)

# Reshape the array to have a shape of 20 elements by 5 elements
array6 = array6.reshape(20, 5)

# Make a copy of array6 and name it array7
array7 = np.copy(array6)

# Multiply each element in array7 by 100
array7 *= 100

# Print the first array (array6)
print("Array6:")
print(array6)

# Print the second array (array7)
print("\nArray7:")
print(array7)
print()

# Answer to Question 5
import pandas as pd

# Create a Pandas Series with specific indices and values
data = [0, 100, 200, 300, 400, 500]
index = ['Column 0', 'Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
obj7 = pd.Series(data, index=index)

# Print the Series
print(obj7)
print()

# Answer to Question 6

import pandas as pd

# Complete the dictionary with the correct data for the DataFrame
data10 = {
    'state': ['Ohio', 'Ohio', 'Arizona', 'Arizona'],
    'population': [1.5, 1.7, 3.6, 4.1],
    'year': [2000, 2001, 2000, 2002]
}

# Create the DataFrame from the dictionary
frame10 = pd.DataFrame(data10)

# Print the DataFrame
print(frame10)


