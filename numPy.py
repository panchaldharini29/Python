# --------------------------
""" NumPy: NumPy is a Python library used for working with arrays.
		   NumPy stands for Numerical Python.
		   In Python we have lists that serve the purpose of arrays, but they are slow to process. 
		   NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
		   The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
		   NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
		   This behavior is called locality of reference in computer science.
		   This is the main reason why NumPy is faster than lists. 
1. Fast, Memory-efficient N-imentional Array
2. It provides foundation for many numerical packages and to integrate python with C/Fortran
	- SciPy : Math algorithms
	- Pandas, Statsmodels : Statistics
	- Matplotlib : Plotting
	- Scikit-image : Image processing
	- Scikit-learn : Machine learning
	- C/Fortran
3. Deep learning frameworks reproduce the NumPy array interface
4. Special array libraries are interperable with NumPy
	- Numpy - Deep Learning Frameworks :PyTorch, TensorFlow, MXNet, JAX
			- Array Advance Libraries : Dasx(Distributed Array), XArray(Labeled Array),CuPy(Arrays on GPUs), PyData/Sparse(Sparse Arrays)
"""

# --------------------------
# Create NumPy Arrays:
# --------------------------
"""
- Load from file: np.load(filename), np.loadtxt(filename) 
- From Python object: np.array(list)
- Zeroes: np.zeros(shape,dtype), np.zeros_like(shape)
A NumPy shape is a tuple of integers, one per dimension
- Random: np.random.random(shape), np.random.randint(min, max, shape), np.random.standard_normal(shape)
"""
# Import required libraries
import math  # Provides mathematical functions
import collections # Provides specialized container datatypes
import dataclasses # Helps in creating classes for structured data
import datetime # For working with dates and times
import numpy as np # NumPy for numerical operations
import pandas as pd # Pandas for data analysis
import matplotlib.pyplot as pp # Matplotlib for plotting/visualization

# Load and inspect text-based image data
lines = open('monalisa.txt', 'r').readlines() # Read all lines from the text file (image data stored as numbers)
print("First Line of the File:", lines[0])  # Print the first line of the file - contains sequence of integers
print("No. of lines in file:", len(lines))  # Print number of lines in the file - 200

# Load numerical data from the text file into a NumPy array
monalisa_bw = np.loadtxt('monalisa.txt')
print("Array:", monalisa_bw) # Print the entire array - 2d array
print("Array's Dimention:", monalisa_bw.ndim)  # Number of dimensions (should be 2D for image) - 2
print("Array's Shape:", monalisa_bw.shape)  # Shape of the array (rows, cols) - 200, 134
print("Array's total no of elements:", monalisa_bw.size) # Total number of elements - 26800
print("Array's no of Bytes in the memory:", monalisa_bw.nbytes) # Memory size (in bytes) -214400
print("Array's datatype:", monalisa_bw.dtype) # Data type of the array - float64

# Display the black-and-white image
pp.imshow(monalisa_bw) # Default color mapping - matplotlib function imshow to a display 2d and numpy array as an image
pp.show()

# Display the image in grayscale
pp.imshow(monalisa_bw, cmap='gray') # gray-scale colour map
pp.show()

# Load binary NumPy image data
monalisa = np.load('monalisa.npy') # Load a saved NumPy array (.npy file) -coloured versiion of painting, saved as numpy's 'native binary format'
print("Image's Dimntion:", monalisa.shape) # Print shape of the array (dimensions of image) - 3D array

# Plot the loaded image with custom figure size
pp.figure(figsize=(5,8))
pp.imshow(monalisa)
pp.show()

# Array creation examples
fromlist = np.array([[1,2,3],[4,5,6],[7,8,9]]) # Create NumPy array from a list of lists
print("Array fromlist:", fromlist)  # Print the array
print("Array's Shape fromlist:", fromlist.shape) # Print shape (3x3)
print("Array's Datatype fromlist:", fromlist.dtype) # Data type of array elements (int) - int64

# Create 1D and 2D arrays filled with zeros
zero_1d = np.zeros(8, 'd')  # 1D array with 8 zeros (dtype = float64)
zero_2d = np.zeros((8,8), np.float64) # 2D 8x8 zero matrix
# Inspect zero arrays
print(zero_1d, zero_1d.ndim, zero_1d.shape, zero_1d.size, zero_1d.nbytes)
print(zero_2d, zero_2d.ndim, zero_2d.shape, zero_2d.size, zero_2d.nbytes)

# Create an array with same shape as monalisa_bw, filled with zeros
print(np.zeros_like(monalisa_bw))

# Create an uninitialized (empty) array of size 24 (values will be random garbage)
print(np.empty(24, 'd'))

# Useful array generation
linear = np.linspace(0, 1, 16) # Generate linearly spaced values between 0 and 1
print(linear)

# Plot the linear values as points
pp.plot(linear, 'o')
pp.show()

# Generate values with a step (like range but with decimals)
print(np.arange(0, 1.5, 0.1))

# Create an 8x8 matrix with random values (0 to 1)
random_2d = np.random.random((8,8))
print(random_2d)

# Visualize the random 2D matrix as a colored grid
pp.matshow(random_2d)
pp.show()

# Generate random integers between 0 and 9 in an 8x8 arra
print(np.random.randint(0, 10, (8,8)))

# Create histogram of 100,000 normally distributed random values
pp.hist(np.random.standard_normal(100000), bins=40)
pp.show()

# Save arrays to disk
np.save('random.npy', random_2d) # Save random_2d array in binary .npy format
np.savetxt('random.txt', random_2d) # Save random_2d array in text format - create a readable ASCII table
print(open('random.txt', 'r').readlines()) # Read back saved text file
