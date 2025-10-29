# --------------------------
# NumPy universal functions
# --------------------------
"""
- Arithmetic: +, -, *, /, **, % (modulus), np.abs, np.sqrt
- Logical/bitwise: & (and), | (or), ^ (xor), ~ (not)
- Trigonometric: np.sin, np.cos, np.tan, np.arcsin, np.arccos, np.arctan, np.arctan2(y,x)
- Hyperbolic: np.sinh, np.cosh, np.tanh, np.arcsinh, np.arccosh, np.arctanh
- Exponential/logarithmic: np.exp, np.log, np.log10
- Miscellaneous: np.isinf, np.isnan, np.round, np.floor, np.ceil

Numpy matches dimentions from the right
Numpy implicitly adds dimentions on the left(with size 1) if needed
Numpy then broadcasts along size 1 dimentions
Users can add dimentions explicitly with np.newaxis
"""
import math
import numpy as np
import matplotlib.pyplot as pp

# ---------------------------------------------------------
# Basic math constants and usage
# ---------------------------------------------------------
print(math.pi) # Prints PI (3.141592653589793)
print(5.0*math.pi) # Multiplying PI by 5

# ---------------------------------------------------------
# Generate evenly spaced values using np.linspace
# ---------------------------------------------------------
# Create an array of 128 values between 0 and 5*PI(inclusive)
x = np.linspace(0.0, 5.0*math.pi, 128)  # extrema are included!
print(x) # This array will be used for plotting sin(x), cos(x), etc.

# ---------------------------------------------------------
# Compare math vs numpy trigonometric functions
# ---------------------------------------------------------
y = 20  # A scalar value
print(math.sin(y)) # math.sin() works only on single numbers (scalars)
siny = np.sin(y) # np.sin() can operate on both scalars and arrays (element-wise)
print(siny)

sinx = np.sin(x) # Apply np.sin() to the full array 'x' (vectorized operation)
print(sinx)

# ---------------------------------------------------------
# Visualize sin(x)
# ---------------------------------------------------------
pp.plot(x, sinx)
pp.show()

pp.plot(x, sinx)
pp.title("Sine Function")
pp.xlabel("x values")
pp.ylabel("sin(x)")
pp.show()

pp.plot(x, sinx)
pp.plot(x, np.cos(x))
pp.plot(x, np.log(1.0 + x))
pp.show()

# ---------------------------------------------------------
# Plot multiple universal functions on the same graph
# ---------------------------------------------------------
pp.plot(x, sinx, label='sin(x)')
pp.plot(x, np.cos(x), label='cos(x)')
pp.plot(x, np.log(1 + x), label='log(1+x)')
pp.legend()
pp.title("sin(x), cos(x), and log(1+x)")
pp.xlabel("x values")
pp.ylabel("Function values")
pp.show()

# ---------------------------------------------------------
# Demonstrating arithmetic operations
# ---------------------------------------------------------
# The power operator in Python is **, not ^ (which is bitwise XOR)
z = y**7 - y**2
print("z=", z)

# ---------------------------------------------------------
# Demonstrate element-wise arithmetic between arrays
# ---------------------------------------------------------
# You cannot slice a scalar (y[16:32] is invalid) → let's create another array
y_array = np.linspace(10, 30, 128)

# Now, element-wise addition between arrays of same shape works fine
c = x + y_array
print("Array addition result:", c)

# Plot to visualize combined data
pp.plot(x, c, label='x + y_array')
pp.legend()
pp.title("Element-wise Addition Example")
pp.show()