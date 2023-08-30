####################Default Arguments, KeyWord Arguments and leveraging them #####################################

#If you have a function where some parameters might not always be required,
# you can use default arguments to provide standard values.

## Default functions. We can mess around and use the = sign. This is so if we 
# Deep Dive into Functions
def create_profile(name, age=30, country="USA"):
    return f"Name is {name}, Age is {age}, and from Country {country}."

def greeting(name="Guest"):
    ## if name is null or nothing in the string. : String no name was given
    # if name is guest give this
    # elif print out the name
    if not name:
        print("String is empty")
    else:
        print(f"{name} is the guest here")
        
greeting(name="Stefanos")
greeting()
greeting(name="")

def exponentialFunction(number, exponent=2):
    return number ** 2

print(exponentialFunction(3, 3))
print(exponentialFunction(2))

def create_profile(first_name, last_name, bio="No bio Provided"):
    return f"{first_name} , {last_name}, {bio}"


print(create_profile("Stefanos", "Sophocleous"))
print(create_profile("Bob", "Smith", "World is my oyster"))

def convert_tempature(temp_in_celsius, scale="fahrenheit"):
    if scale == "fahrenheit":
        result = temp_in_celsius * 9/5 + 32
        return result
    elif scale == "kelvin":
        result = temp_in_celsius + 273.15
        return result

print(convert_tempature(30))
print(convert_tempature(30, "kelvin"))

##########  END Section #####
### Variable Length arguments ###########

def print_all(*args):
    for arg in args:
        print(arg)
#print_all(1, 2, 3, 4)

# *args positional argument
# ** kwargs for keyword arguemnt
############ Lambda Map Filter Reduice ###############
# lambda practice
# Secon half of it is the return
add = lambda x: x + 10
print(add(10))

multipleArgs = lambda first_name="Stef", last_name="Soph": f"{first_name, last_name} is the first and last name"
print(multipleArgs())
print(multipleArgs("Bob", "Smith"))

nums = [1, 2, 3, 4,]

 
 ############################## MAP FUNCTION ###########################
 ## map(function, iterable,)
 # function execute for each item
 # iterable( like a list tupe etc. on which is applied on every time)
print('__________________MAP FUNCTION WORK_______________________')
print('')
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))

words = ["apple", "banana", "cherry"]
uppercased = map(str.upper, words)
print(list(uppercased))  # Outputs: ['APPLE', 'BANANA', 'CHERRY']




## WITH DEF  BAD practice
def squaredfunc(x):
    return x**2


SquaredFunction = map(squaredfunc, numbers)
print(list(SquaredFunction))
#################################################################################

##############################   Filter Function ###########

## filter(function, iterable)
# function (The function to test each element in the iterable, Should return either True or false)
# Iterable ( THe iterable whose elments you want to filter)
numbers = [1, 2, 3, 4]
squared = filter(lambda x: x**2, numbers)
#print(list(f"{squared} filter"))  # Outputs: [1, 4, 9, 16]


# MAP () for transformation
# FILTER FOR SELECTION


############# Practice Questions #######################

wordBank = ["Stefanos", "Billy", "Jon", "Wuhaaa", "Hero", "Testing", "Kappa Pog"]
#  **TODO: MAP() Convert Numbers to Strings leveraging MAP(),
numToString = list(map(lambda num: str(num), numbers)) # Take a list of numbers and turn them into a list of strings
print(numToString)










#**TODO: Capitalize All words Map(). 
'''
upperCaseWords = list(map(lambda words: words.upper(), wordBank))
print(upperCaseWords)
'''

# **TODO: Capitalize Every other charachter ()
#def retrieveEveryOtherWord():

#Go over each word in the wordbank. 
#Every other word so 1 3 5 etc. Grab that value. and take the second position of the string and uppercase then add it to the list.

def retrieveEveryOtherWord():
    # So i want to set a counter List. For every other word lets add it into this list.
    # Then I upper case the LIst and we return it to the user
    templist = []
    for index, value in enumerate(wordBank):
        #print(index, value)
        if index % 2 != 0:
            print(f"{index} {value}")
            print(value[0])
            templist.append(value[1].upper())
    
    return templist
print("___________________")
print(retrieveEveryOtherWord())     
    



tempData = [
    "123-45-6789",   # Matches format
    "apple",         # Random word
    "456-78-9012",   # Matches format
    "ProStar",       # Random word (which you might want to capitalize)
    "orange",        # Random word
    "789-01-2345",   # Matches format
    "banana",        # Random word
    "999-99-9999",   # Matches format
    "grape",         # Random word
    "pineapple"      # Random word
]

# **TODO: If the word contains the format xxx-xx-xxxx it to a ProStar and then capitilize the others Filter() 
#



# **TODO: convert a list of values to KEY VALUE PAIRS in a DICTIONARY, 
def listToDict():
    my_dict = {}
    for index, element in enumerate(tempData):
        my_dict[index] = element
    print(my_dict)


print(listToDict())

def caculatePositive(num):
    if num > 0:
        return num
    else:
        False


#**TODO Leverage Filter() to handle Positive numbers only
numbers = [-1, 5, -3, 2, -7, 4, 6]
# Use filter to extract only the positive numbers.
positiveNumbers = filter(lambda num: num > 0, numbers)
                   #    numToString = list(map(lambda num: str(num), numbers)) # Take a list of numbers and turn them into a list of strings
print('____________')
print(list(positiveNumbers))


#**TODO Filter() for Email Addresses
emails = ["john@examplfe.com", "anna@gmail.org", "mike@exampfle.com", "susan@yahoo.com", "tom@exafmple.com"]
# Use filter to extract emails that end with "@example.com".

filterEmail = list(filter(lambda email: email.endswith("@example.com"), emails))
if not filterEmail:
    print("There were no emails found ending with this address")
else:
    print(filterEmail)

#print(filterEmail)


products = [
    {"name": "apple", "price": 0.5},
    {"name": "banana", "price": 0.25},
    {"name": "cherry", "price": 15},
    {"name": "date", "price": 3},
    {"name": "elderberry", "price": 20}
]
# Use filter to extract products priced below $10.
entire_list = products[:]
#print(products[0][1])
#print(entire_list)


    
#**TODO Product Below a Price
# 
priceBelow10 = list(filter(lambda product: product["price"] > 10, products))

def get_price(priceBelow10=None):
    try:
        if not priceBelow10:
            print("WHoa there is nothing within that price range")
        return priceBelow10
    except:
        pass
print(priceBelow10)


#print(retrieveProducts)
#**TODO