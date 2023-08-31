################Tuples Practice##############T
'''
short_tuple = ("rofl,", "Bob"
               "Anne")  ## Tuple. Not required for brackets

# Adding to tuple
short_tuple = short_tuple + ("Jen",)
print(short_tuple)

#print(short_tuple)
tuple_in_list = [("Rofl", "Bob")]  ## Tuple in list.

## Tuples when you want to keep them
# Most time use tuples over list. only list when use changes.

'''

#############################################

##################Sets Practice ###########
## Sets dont contain order and duplicate order.
'''
art_friends = {"Rolf", "Anne", "Jen"}  #Set
science_friends = {"Jen", "Charlie"}
#art_friends.add("Jen")
#print(art_friends)
#art_friends.remove("Jen")

# Sets are great to compare whats in one and not the other
art_not_science = art_friends.difference(science_friends)
science_not_art = science_friends.difference(art_friends)
print(art_not_science)
print(science_not_art)
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# . Difference element in one not the other
# SymetricDifference element that are not in both

art_and_science = art_friends.intersection(science_friends)
print(art_and_science)

# join sets.
all_friends = art_friends.union(science_friends)
print(all_friends)
'''

################ Dictionaries #######################
'''
## Store key and Values usedful for when I know the key and wan the value back
friends_ages = {"Rolf": 24, "Adam":30, "Anne": 27}
print(friends_ages["Rolf"]) # Give me back 24 cuz i gave the key
friends_ages["Bob"] = 20
friends_ages["Rolf"] = 25
print(friends_ages)

# Dictoinaries to keep the order, We cant have duplicate keys though...
#Tuple with 3 dictionary objects inside
friends = (
        {"name": "Rolf Smith", "Age": 24},
        {"name": "Adam Wool", "Age": 30},
        {"name": "Anne Pun", "Age": 27},
)
# This is cool if i want to access the element then the Name lets say. 
# Always access the same key.
print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

friends = [("Roilf", 24), ("Adam", 30), ("Anne", 27)] # List of tuples
friends_ages = dict(friends) ## Dict is used to conver it to a dictoinary object
print(friends)
'''
################ Dictionaries #######################

################## Len & Sum ####################
''''''
grades = [80, 75, 90, 100]
total = sum(grades)
print(total)

length = len(grades)
print(length)
average = total / length
print(average)
### [] -> List, () -> tuple , {} -> set
grades = [80, 75, 90, 100] ## List easiest
grades = (80, 75, 90, 100) ## Tuple if we don tneed to add. 
grades = {80, 75, 90, 100} ## Sets Compare grades
'''
################## Len & Sum ####################

'''
friends = ["Rolf", "Anne", "Charlie"]
comma_seperated = ", ".join(friends) # comma and space is used as the seperator
print(f"My friends are {comma_seperated}")


################## While #################

is_learning = True

while is_learning: 
    print("your learning")
    user_input = input("Are you still learning")
    is_learning = user_input == "yes"

print("We stopped running")
'''
#######################################
'''
for index in range(5,10): # this will give you the numbers 5 up to 10
    print(index)

    
for index in range(2,20,3): # this will give you the numbers 2 - 20 but counts by every 3
    print(index)



students = [ ## List of dictionary Objects
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 20},
    {"name": "Jen", "grade": 40},
]
for student in students:
    name = student["name"] # get the name key of each value
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")


'''
##########Destructuring####################
'''
currencies = 0.8, 1.2
usd, eur = currencies
print(usd, eur)
'''
############ Iterating over Dictionaries ############
'''
friends_ages = {"Stef Smith": 18, "John Smith": 15,"George Smith": 233}
for name in friends_ages:  #Iterating over the dictionary Keys when i do it like
    print(name)

for name in friends_ages.values():  #Iterating over the dictionary Values when i do it like
    print(name)

for name, age in friends_ages.items():# Keys and Value we can get them like htis Items allow us to break it down. Items veyr popular dictionary
    print(f"{name} is {age} years old")
'''
############## Break / Continue ####################

# break when you wan tto terminate the loop completely.
# continue it just goes into the next one to the top. The next iteration
'''
cars = ["ok", "ok", "ok", "ok", "ok", "ok"]


for status in cars:
    if status == "faulty":
        print("Found faulty car, Skipping...")
        break #Goes
    print(f"This car is {status}")
    print(f"Shipping new car to customer")
else: ## if loop ran without no errors
    print("All cars bulit sucessfully . No faulty Cars") ## this iwll validate the 

## Prime Numbers with for loops
for n in range(2, 10):  # Start at 2 go up to 10 then stop
    for x in range(2, n): # so it goes from 2 up to the number of our top loop
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break
    else:
        print(f"{n} is a prime number")
'''
        
############## Slicing ####################

'''
friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
print(friends[2:4])
print(friends[:4]) #Start of the list 

print(friends[:]) #Your not getting the same list but you get the whole thing back

print(friends[-3:])  # starting from the end. The 3rd one. 

'''
############## List Comprehension ######################
'''
numbers = [0,1,2,3,4]
double_numbers = []

doubled_numbers = [number * 2 for number in numbers] ## Syntax like this to create into the new list
print(double_numbers)

friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} yeras old " for age in friend_ages]
print(age_strings)

names = ["Rof", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

friendName = input("Enter your friend name")
BestFriends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
friends_lower = [name.lower() for name in BestFriends] # one way 

if friendName.lower() in friends_lower:
    print(f"{friendName} is one of your friends")

print(friendName.title()) #Capitilizes first letter

'''
################### Comprehension with Conditionals #############################
#ages = [22, 31, 35, 37]
#odds = [age for age in ages if age % 2 == 1] # only will work if the ocnditional is met
#print(odds)
'''

friends = ["Rolf", "charlie", "Anna", "Bob", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "Michael"]
friends_lower = [f.lower() for f in friends]

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]
print(present_friends)

