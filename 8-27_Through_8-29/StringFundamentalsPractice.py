# Basic Manipulation
word = "The world is a great place"
wordDict = [
            {"name": "Befanos"},
            {"name": "Whoa"},
            {"name": "Rona ld"},
            {"name": "Hero"},
            {"name": "1234 F"},
            {"name": "1555"}
]
# Upper case words if they contain a length greater than or = 4
# Working with Dictionary.
for index, data in enumerate(wordDict):
   # if len(data['name']) >= 4:
      #   print(f"{index}, {data['name'].upper()}")
    if data['name'].isalpha():
        print(data)
        
    




# upper()  -> Converts all charachters in string uppercase
#print(word.upper()) 

#lower() -> Converts all to lowercase
#print(word.lower())

#title() -> converts the first charachter of each word to uppercase.
#print(word.title())

#-------------------------------------------------------------------------


# Checking String Properties
#print(word.isalpha()) # -> returns True / False. If alphabetic True. Else False

#print(word.isdigit()) # -> return True if all charachters are digits otherwise false


#Searching & Replacing

tempWord = "    Here in the Cyber Office 123   "
social = "183-98-3912"
# Searching
print(tempWord.find("i")) #Finds the first index of this 

## Searching and Replacing is crucial.
print(tempWord.replace("i", "**"))
ssn = "123-45-6789"
mask_char = 'X'

for digit in '0123456789':
    ssn = ssn.replace(digit, mask_char)
    
    
print(ssn)


#### Trimming
# Lets remove all the white space and a number
print(tempWord)
print(tempWord.strip()) # Leading and Trailing white spaces removed. 

## Splitting and Joining  tempWord = "    Here in the Cyber Office 123   "
splitWords = tempWord.split() # --> ['Here', 'in', 'the', 'Cyber', 'Office', '123']
print(splitWords)

joinedWords = " ".join(splitWords)
print(joinedWords) #--> HereintheCyberOffice123




##**TODO Exercises :
'''
replace()

Problem: Given a paragraph of text, replace all instances of the word "good" with "excellent" and all instances of the word "bad" with "terrible".
Sample Input: "It was a good day but the weather was bad."
Sample Output: "It was an excellent day but the weather was terrible."
'''
def replacePractice():
    sampleInput = "It was a good day but the weather was bad."
    
    data = lambda x: x.replace('good', 'excellent').replace("bad","terrible")
    result = data(sampleInput)
    print(result)
    #print(test)
replacePractice()

##words = ["apple pie", "apple tart", "fresh apple", "apple cider"]

#modified_words = list(map(lambda x: x.replace("apple", "orange"), words))

'''
strip()

Problem: You have a list of strings, each representing a word. However, some words have extraneous spaces before or after them.
Write a function to return a list of words without any leading or trailing spaces.
Sample Input: [" apple", "banana ", " cherry ", "date"]
Sample Output: ["apple", "banana", "cherry", "date"]
'''
Sample_Input = [" apple", "banana ", " cherry ", "date"]
cleanList = [word.strip() for word in Sample_Input]
'''
split()

Problem: Given a string representing a CSV (Comma-Separated Values) row, split the string into a list of individual values, 
taking into account that values might be wrapped in quotes (which should be excluded in the result).
Sample Input: 'John, "Doe, Jr.", 25, "New York"'
Sample Output: ['John', 'Doe, Jr.', '25', 'New York']
Note: This problem is a simplified version of parsing CSV data. In a real-world scenario, CSV parsing can be more complex, especially if values can contain escaped quotes.
'''
SampleData ='John, "Doe, Jr.", 25, "New York"'
splitData = SampleData.split(", ")
print(data)
'''
join()

Problem: You're given a list of words. Concatenate them into a single string where each word is separated by a comma and a space. However, before the last word, add the word "and".
Sample Input: ["apple", "banana", "cherry"]
Sample Output: "apple, banana, and cherry"
'''