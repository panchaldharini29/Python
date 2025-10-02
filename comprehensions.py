"""
Comprehensions in Python provide a concise and efficient way to create new sequences from existing ones. 
They enhance code readability and reduce the need for lengthy loops.
They provide a more "Pythonic" and often more readable alternative to traditional for loops with append() operations, or map() and filter() functions.
"""

# create a list of squares using a for loop
squares = []
for i in range(1, 11):
    squares.append(i**2)
print(squares)  # [1, 4, 9, 16, ..., 100]

# same as above but using list comprehension
squares2 = [i**2 for i in range(1, 11)]
print(squares2) # [1, 4, 9, 16, ..., 100]

# list comprehension with condition:
# include squares only if divisible by 4
squares_by_four = [i**2 for i in range(1, 11) if i**2 % 4 == 0]
print(squares_by_four)  # [4, 16, 36, 64, 100]

# dictionary comprehension: key = number, value = square
squares_dict = {i: i**2 for i in range(1, 11)}
print(squares_dict)  # {1:1, 2:4, 3:9, ..., 10:100}

# invert a dictionary using dict comprehension
capitals_by_country = {'United States': 'Washington, DC', 'France': 'Paris', 'Italy': 'Rome'}
countries_by_capital = {capital: country for country, capital in capitals_by_country.items()}
print(capitals_by_country) # original dictionary
print(countries_by_capital)  # inverted dictionary

# generator expression (lazy evaluation):
# sum of squares from 1 to 10
print(sum(i**2 for i in range(1, 11)))  # 385

# nested list comprehension: build a 3x3 multiplication table
matrix = [[i*j for i in range(1,4)] for j in range(1,4)]
print(matrix) # [[1,2,3], [2,4,6], [3,6,9]]

# flatten the matrix (convert 2D → 1D list)
print([element for row in matrix for element in row]) # [1, 2, 3, 2, 4, 6, 3, 6, 9]