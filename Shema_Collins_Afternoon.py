# Exercise 1.
dict = {
    'name': 'Mercedes',
    'age': 12,
    'country': 'Germany'}
# Using the values() method to get values.
dict_list = list(dict.values())
print(dict_list)

# Exercise 2.
# How to check if a key exists in a dictionary
if 'age' in dict:
    print("Age exists in the dictionary")

# Exercise 3
# How to change dictionary items and update them
dict['age'] = 20

# Exercise 4
# Example on how to add an item in a dictionary
dict['model'] = 'g-wagon'
print(dict)


# Exercise 5
# How to loop through and nest dictionaries
# Looping through a dictionary
for item in dict :
    print(item)
# Nest dictionaries
dict2 = {
    'name': 'Scott',
    'class':'Year 2',
    'units':{'unit1': 'BSSE', 'unit2': 'BIST', 'unit3': 'CS'}
    }
print(dict2['units']['unit1'])

#STRINGS
# Exercise 1
name = "Richard"
print(len(name))

# Exercise 2
for x in name:
    print(x)
print('Next is string slicing')
# Exercise 3
# String slicing
print(name[2:5])