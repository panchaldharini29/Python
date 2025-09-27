# Lists: Used to store ordered multiple values in single variable, of any or multiple data type. It can contain duplicate values. index based strats from 0.

listA = [1, 3.2, 2, "abc", False, True, 23]
print("List:",listA)
print("List value at index 3:",listA[3])
print("Lenghth of list listA:",len(listA))
print("Verify if value exist in listA:",3.2 in listA)

# insert single value in list use listname.append(value)
listA.append("duck")
print("Updated listA:", listA)

# insert multiple elements at once in list use listname.extend([value1, value2, ...., valuen])
listA.extend(["Swan", 45, 32])
print("Upated listA:", listA)

# concate 2 different lists
list2 = ["hi", "string", 92]
listA2 = listA + list2
print("ListA2:",listA2)
listA3 = list2 + ["doll", "kite"]
print("listA3:", listA3)

# insert element at specific postion in list use listname.insert(index, 'value')
list2.insert(0,"one")
print("updated list2:", list2)

# delete element at specific index from list use del listname(index)
del listA3[2]
print("updated listA3:", listA3)

# delete using value in list use listname.remove('value')
listA3.remove('string')
print("updated listA3:", listA3)

# sort the list
numbers = [1, 6, 4, 97, 45, 24]
print("Before sort:",numbers)
numbers.sort()
print("After sort:",numbers)

fruits = ["apple", "kiwi", "mango", "fig", "peach", "orange"]
print("Before sort:",fruits)
fruits.sort()
print("After sort:",fruits)

# reverse sort
reversefruits = sorted(fruits, reverse = True)
print(reversefruits)

# loop 
for fruit in fruits:
	print(fruit)

# slicing a list
squares = [1, 4, 7, 9, 13, 18, 25, 30]
print("slicng with starting and ending index:",squares[0:2])
print("Slicing with ending index:",squares[:4])
print("Slicing from starting index:",squares[6:])
print("Entire list:",squares[:])
print("Steped sliced list:",squares[0:7:2])
print("Slicing from back:",squares[-3:-1])
print("Reverse list:",squares[::-1])
squares[2:4] = ["Four", "Nine"]
print("Ressign value:",squares )
del squares[4:6]
print("Delete value:", squares)

print(type(fruits)) #fruits' datatype - list: <class 'list'>
