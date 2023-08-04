#Operations on sets
#The set we are to work on
houses = {"Pearl","Golden","Mbaguta","Africa"}
#To find the length of a set
print(len(houses))
#How to access an element of a set
#We can use the in keyword to check if it's there
#But set elements are unordered so we cant easily access an element using indexes
#We can convert it to a list look for what we want then turn it back
house_list=list(houses)
print(house_list[1])
houses=set(house_list)
print(houses)
#Add items in a set
houses.add("Crichton")
print(houses)
#Removing an element
houses.remove("Golden")
print(houses)
#Checking for the datatype of your set
print(type(houses))
# Adding two sets together
halls = {"Mitchell","Nsibirwa","Lumumba"}
all_houses = houses.union(halls)
print(all_houses)