# Exercise 1

names=["Sam","Delton","Willing","Fred","Balaaba"]
print(names[1])
names[0]="Eddie"
names.append("Eddie")
names.insert(2,"Bathel")
names.pop(3)
print(names[-1])

# printing items at 3,4,5.
cars = ["Benz","Volvo","Tesla","BMW","Prado","Audi","Jeep"]
car_number = [3,4,5]
for car in car_number:
    if 0<= car <= len(cars):
        print(cars[car])

# List of countries
countries = ["Algeria","Rwanda","Kenya","America","Wales"]
countries.copy()

# Loop through countries
for country in countries:
    print(country)

# Animal names
animals = ["Max","Webber","Simba","Tigre","Alexy"]
animals.sort() # ascending order
animals.sort(reverse=True) # Descending order
# with letter "a"
letter="A"
for animal in animals:
    if animal.startswith(letter):
        print(animal)

# Joining lists
first_names = ["Aine","Karamagi","Shema"]
last_names = ["Collins","Smith","William"]
first_names.extend(last_names)


# EXERCISE 2
#Tuples

x = ("samsung","iphone","tecno","redmi")
print(x[0])

#Print the second last
print(x[-2])

# Update iphone
phone_list = list(x)
phone_list[1] = "itel"
x=tuple(phone_list)
new_phone = ("Huawei")
x += new_phone

# Loop through phones
for phone in x:
    print(x)

#remove an item
phone_list1 = list(x)
phone_list1.remove("samsung")
x = tuple(phone_list1)

#Using tuple constructor
cities = tuple(('Mbarara', 'Fort Portal', 'Lira', 'Kampala', 'Jinja'))
#Unpack a tuple
city1, city2, city3, city4, city5 = cities
print(city1)
print(city2)
print(city3)
print(city4)
print(city5)
# loop through cities
for city in range(1, 4):
    print(cities[city])

#Colors and multiply
colors = ('red', 'blue', 'green')
colors_three= colors * 3

thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))


# EXERCISE 3
# SETS
beverages = set(["milk","ikivuguto","porridge"])
print(beverages)
beverages.add("water","juice")

# check if an element is in a set
my_set = {"oven","kettle","microwave","refrigerator"}

if "microwave" in my_set:
    print("Microwave is in the set")
else:
    print("the microwave is not there")
# Remove an element
my_set.remove("kettle")
# Loop through the set
for element in my_set:
    print(element)

# Adding list elements in a set.
set1 = {1,2,3,4}
list1= [5,6]
set1.update(list1)

name_set = {"Camie","Welni"}
age_set = {24,20}
name_set.union(age_set)


# EXERCISE 4
a = 20
b = "class"
ab = b + str(a)

# Remove whitespaces
txt = " Hello, Uganda! "
txt.strip()
#Uppercase
capital = txt.upper()
#Replacing
new_txt = capital.replace("U", "V")

#Character in 2nd, 3rd, 4th
y = "I am proudly Ugandan"
characters = y[1:4]

# Correcting code
z = "All Data Scientists are cool!"


# EXERCISE 5
# DICTIONARIES
shoes = {
    "brand":"Nick",
    "color":"black",
    "size":40
}
print(shoes["size"])
# Change value
shoes["brand"] = "Adidas"
shoes["type"] = "sneakers"
#list of shoe value
shoe_list = list(shoes)
print(shoe_list)
shoe_values = list(shoes.values())
print(shoe_values)
# check if a key exists
if "size" in shoes:
    print("The key size exists")

#loop through a dictionary
for shoe in shoes:
    print(shoe)

# Remove an element
shoes.pop("color")

# Empting a dictionary
shoes.clear()

# Copying  a dictionary
players = {
    "name":"Ronaldo",
    "position":"Goat"
}
players.copy()

# Showing nested dictionaries
dict2 = {
    'name': 'Scott',
    'class':'Year 2',
    'units':{'unit1': 'BSSE', 'unit2': 'BIST', 'unit3': 'CS'}
    }
print(dict2['units']['unit1'])