"""tuples: Tuples are used to store multiple items in a single variable. 
		   A tuple is a collection which is ordered, unchangeable and allow duplicate values.
		   Tuples are written with round brackets. 
		   tuplename = (val1, val2, ..., valn)"""
integers = ('one', 'two', 'three', 'four', 'five', 'six')
print(integers)

# slicing tuples
print(integers[-1], integers[1:3])

# Wouldn't work as tuples are unchangable
# integers[0] = 1

# unpack tuple (1, 2) into variables a and b
(a,b) = (1,2)
print(a) #1
print(b) #2

# multiple assignment (same as tuple unpacking)
c,d = 3, 4
print(c) #3
print(d) #4

"""enumerate(): It is a built-in Python function that adds an index counter to an iterable (like a list, tuple, or string)
				It basically gives you: the index (position number) and the value (element itself)"""

# tuple loop
# # iterate tuple with index and value
animals = ('cat', 'bat', 'dog', 'ant', 'ell', 'pig', 'rat')
for i, animal in enumerate(animals):
	print(i, animal)

# iterate tuple (values only)
for animal in animals:
	print (animal)

# iterate tuple with index and value (returned as tuple)
for animal in enumerate(animals):
	print (animal)

# define a function that takes 3 arguments
def printThreeArguments(a,b,c):
	print("A:",a,"B:",b,"C:",c)
# create a tuple with 3 elements
myArguments = ('red',2,"study time")
# unpack the tuple into separate arguments using *
# equivalent to: printThreeArguments('red', 2, "study time")
printThreeArguments(*myArguments)

# define a function that takes any number of arguments
def anyNoOfArguments(*args):
	print(args)
anyNoOfArguments(0, 5, 7, 9, "lion")