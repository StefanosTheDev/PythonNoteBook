## A function that tets if elements of an iterable return true or false. If None, it simply returns the elmenets of iterable that are true. 
#Iterable: An Iterable like sets tuples and lists etc.

def is_even(num):
    return num % 2 == 0

# list of num
numbers = [1,2,3,4,5]

# Leverage the filter to apply the function to the list.
filtered_numbers = filter(is_even, numbers)

print(f"{filtered_numbers} This is the return from the filter function")
# convert the iterator returned by filter into a list (True)

filtered_numbers_list = list(filtered_numbers)

print(filtered_numbers_list)


# Now leverage Lambda. # this can be great for quick throwaway functions that i dont need to re use other places. 
filt_lambda = filter(lambda num: num % 2 == 0, numbers)

print(list(filt_lambda))


################################ More Notes  #################################################
'''' 
Leverage None as a function. 

Performance Consideration. For Large data sets . Filter() can be more memory efficeint thatn a list comprehesion because it retruns an iterator than a list. 
However if i need to reuse that return than a list or tuple more effective 
'''

########### Practice Problems Filter() ##########################################
def positive_num_filter():
    numbers = [-10, -5, 0, 5, 10]
    pos_num = filter(lambda num: num > 0, numbers)
    print(f"Positive Numbers in the list are {list(pos_num)}")


''' 
The trim() method of String values removes whitespace from both ends of this string and returns a new string, without modifying the original string.
'''
def filter_even_words():
    words = ["he                     llo", "world", "python", "is", "awesome", "Stef", "Odd"]
    ## iterate through the list and remove white space. 
    ## Once whitespace is removed in each word. looka t the length. then if that length is modules 2 for example right so no remainer then its even
    even_list = []
    odd_list = []
    for w in words: 
        new_w = w.replace(' ', '') ## Take the white space '  ' and replace it with an empty string
        if len(new_w) % 2 == 0: # Check if after you divide by 2 if there is a remainder.
            even_list.append(new_w)
        else: 
            odd_list.append(new_w)
    return even_list, odd_list

'''
### This is the GPT explanation for this ###

Removed the enumerate: Since you're not using the index i, there's no need for enumerate().
Direct check in if statement: Instead of creating a list of vowels to remove in each iteration, it directly checks if the character is a vowel and adds it to the list.
Set conversion: Before returning, it converts the list to a set to remove any duplicate vowels and then converts it back to a list.
Return statement placement: The return statement is now outside the loop, so it returns the full list after the loop has completed.

###
'''
def filter_vowel():
    sentence = "Filtering vowels in this sentence."
    char_to_remove = []  # Initialize as an empty list
    vowel_list = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    
    
    # This is great because the equivialent was :
    '''
    for char in sentence:
    if char in vowel_list:
        char_to_remove.append(char)

    '''
    
    char_to_remove = [char for char in sentence if char in vowel_list]

    # Convert to a set to remove duplicates and then back to a list
    char_to_remove = list(set(char_to_remove))

    # Create a new sentence with vowels removed *** This is a critical line
    '''
    "Let's create a new sentence that includes only those characters from the original sentence that are not vowels,
    and let's make sure those characters are joined together without any additional characters in between."
    '''
    new_sentence = ''.join([char for char in sentence if char not in char_to_remove])

    return new_sentence


def remove_empty_elements():
    strings = ["Python", "", "Coding", " ", "is", "", "Fun"]
    pass

def filter_valid_email():
    emails = ["user@example.com", "invalidemail", "another@domain.com"]
    pass

'''
data = filter_even_words()
print(f"The even list is {data[0]}")
print(f"The Odd list is {data[1]}")

'''
filtered_sentence = filter_vowel()
print("Original sentence: Filtering vowels in this sentence.")
print("Filtered sentence:", filtered_sentence)