print("hey")

# Dictionaries are used to store data values in key:value pairs. 
# A dictionary is a collection which is ordered, changeable and do not allow duplicates. 
# Dictionaries are written with curly brackets, and have keys and values: dictionaryName = {key1:val1, key2:val2,...,keyn:valn}

colors = {
	"plant":"green", 
	"sky":"blue", 
	"paper":"white",
	"blood":"red"
}
print(colors) #retrive dictionary
print(len(colors)) #get length of dictionary
print(len({})) #empty dictionary length check

#add single value
colors["pig"] = "pink"

print(colors["blood"]) #fetch value bind with specific keys
print("sky" in colors, "hair" in colors) #check if elemt exist in dictionary

#unpacking using **
moreColors = {
	"sun":"yellow",
	"water":"transparent"
}
{**colors, **moreColors} #unpack both dictionaries into a new one (does not change the original)
colors.update(moreColors) #update 'colors' dictionary by appending key-value pairs from 'moreColors
print(colors) #print updated dictionary

#delete items using keys
del colors['pig']
print(colors)

#create a dictionary with tuples as keys (month, day) → name
birthdays = {(7,15): 'Michele', (3,14): 'Albert'} 
birthdays[(7,15)] #access the value for key (7, 15) → 'Michele'
print(hash('Italy'), hash((7,15)))  # hash of a string and a tuple

#loop
print("Values:",colors.values())
print("Keys:",colors.keys())

#looping through values of dictionary
for color in colors.values():
	print("Value:",color)

#looping through keys of dictionary
for color in colors.keys():
	print("Key:",color)

#convert dictionary to list
print(list(colors.keys()))

#key:value pair loop
for colorVal, colorKey in colors.items():
	print(colorVal, colorKey)

# key:value pair loop
print(colors.items())

print(type(colors)) #colors' datatype - dictionary