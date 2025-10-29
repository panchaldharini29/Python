# --------------------------
# Slicing and Indexing in NumPy:
# --------------------------
"""
- Basic Slicing: array[start:stop:step] (omit any for shortcut)
- Assignment: array[start:stop:step] = value or array
- Multi-Dimensional Slicing: array[start1:stop1:step1, start2:stop2:step2, ...]
- Boolean Indexing: array[condition] (e.g., array[array > 0])
- Fancy Indexing: array[[indices]]
"""

import numpy as np
import matplotlib.pyplot as pp

monalisa = np.load("monalisa.npy") # Load a color image (NumPy .npy format)
print(monalisa.shape) #3d array (height, width, color for RGB image)-> (1198, 804, 3)

# Display the full image
pp.imshow(monalisa) 
pp.show()

# ---------------------------------------------------------
# Accessing elements
# ---------------------------------------------------------
# Access a single pixel (R, G, B components)
# monalisa[y, x, color_channel]
monalisa[600, 400, 0] # Access the red channel value at (600, 400)

# Convert NumPy number to standard Python int/float
print(int(monalisa[600, 400, 0]), float(monalisa[600, 400, 0])) #247,247.0

# Accessing pixels using negative indices (counting from the end)
print(monalisa[-50, -50, 1])  # Green channel near bottom-right corner->11
print(monalisa[1148, 754, 1]) # Same as above with positive indices->11
# print(monalisa[1000, 900, 2]) # Blue channel at specific coordinates- index out of bound error

# Modify a specific pixel — set RGB values to black (0)
monalisa[600, 400, 0] = monalisa[600, 400, 1] = monalisa[600, 400, 2] = 0

# ---------------------------------------------------------
# List vs NumPy array slicing
# ---------------------------------------------------------
just_a_list = [[1,2,3],[4,5,6],[7,8,9]] # Regular Python list (2D)

# just_a_list[1,2] → invalid syntax for lists, must use double brackets:
print(just_a_list[1])      # Access 2nd row → [4,5,6]
print(just_a_list[1][2])   # Access element 6 in 2nd row ->6

# ---------------------------------------------------------
# Array slicing examples
# ---------------------------------------------------------
# Slice a portion of the image: rows 400–800, columns 200–600
pp.imshow(monalisa[400:800, 200:600, 0:3])
pp.show()

# Lower half of the image
pp.imshow(monalisa[800:, :, :])
pp.show()

# Slice rows 100–400, include all columns and channels ("..." means all remaining dims)
pp.imshow(monalisa[100:400, ...])
pp.show()

# Downsample the image — every 20th pixel in both directions
pp.imshow(monalisa[::20, ::20, :])
pp.show()

# Flip the image vertically (reverse row order)
pp.imshow(monalisa[::-1, :, :])
pp.show()

# ---------------------------------------------------------
# Working with rows and subregions
# ---------------------------------------------------------
row = monalisa[20, ::20, 0] # Select one row (y=20) — every 20th pixel, red channel
print(row.shape) #(41,)
pp.plot(row) # [[104  81 107 100  90  98  94 103 103  97  99 105 116 100  90  97  85  97  93  97 104  94  85 112  92  98  88  81 106  79  80  91  82 100 104  8888  79  81  81  88]]
pp.show() 

# Extract a thin rectangular slice (height=1)
rect = monalisa[20:21, ::20, 0]
print(rect) #(1, 41)
print(rect.shape) 

# Modify a rectangular region: set color to medium gray (200)
monalisa[20:300, 20:300, :] = 200
pp.imshow(monalisa) 
pp.show()

# Replace that same region with random colors (values between 100 and 255)
monalisa[20:300, 20:300, :] = np.random.randint(100, 255, size=(280, 280, 3))
pp.imshow(monalisa)
pp.show()

# ---------------------------------------------------------
# Working with black-and-white images
# ---------------------------------------------------------
monalisa_bw = np.loadtxt('monalisa.txt') # Load grayscale image data
pp.imshow(monalisa_bw, cmap='gray') # Display as grayscale
pp.show()

mask = monalisa_bw < 120 # Create a boolean mask for values less than 120
"""->[[ True  True  True ...  True  True  True]
 [ True  True  True ...  True  True  True]
 [ True  True  True ...  True  True  True]
 ...
 [ True  True  True ...  True  True  True]
 [ True  True  True ...  True  True  True]
 [ True  True  True ...  True  True  True]]"""
print(mask)  # Shows True/False matrix 

monalisa_bw[mask] = 0 # Set all dark pixels (<120) to black (0)

pp.imshow(monalisa_bw, cmap='gray') # Display the thresholded image
pp.show()

# ---------------------------------------------------------
# Python list vs NumPy slice behavior
# ---------------------------------------------------------
mylist = [0,1,2,3,4,5] # Simple list slicing example
myslice = mylist[0:4]  # Creates a shallow copy (new list)
myslice[2] = myslice[3] = 100
print(myslice) # [0,1,100,100]
print(mylist) # Original list unchanged → [0,1,2,3,4,5]

# NumPy slicing creates a *view*, not a copy
monaslice = monalisa[:, 300:500, :]  # Subregion of image
pp.imshow(monaslice)
pp.show()

# In-place modify values (divide color intensity by 3)
monaslice[:,:,:] //= 3 # integer-divide by three in place
pp.imshow(monalisa)
pp.show()

monacopy = monalisa_bw.copy() # To prevent modifying the original array, use copy()

# when you slice a list in python, you create a copy of it