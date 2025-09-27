"""Sets: Sets are used to store multiple items in a single variable.
		A set is a collection which is unordered, unchangeable, unindexed and no duplicates.
		Set items are unchangeable, but you can remove items and add new items.
		Sets are written with curly brackets. setName = {val1, val2,..., valn}
"""
# create a set (unordered collection of unique items)
foods = {'icecream', 'pizza', 'burger', 'fries', 'chips', 'cake', 'icecream', 'pizza'}

print("Set:",foods) # print the whole set (order may vary since sets are unordered)

print("Check if item exist in set:",'pizza' in foods) # check if an item exists in the set

# add a new item to the set
foods.add('tacos')
print("Added an item:",foods)

# remove an item from the set
foods.remove('fries')
print("Removed an item:",foods)

# iterate through the set (order is not guaranteed)
for food in foods:
	print (food)

print(type(foods)) #foods' datatype - set