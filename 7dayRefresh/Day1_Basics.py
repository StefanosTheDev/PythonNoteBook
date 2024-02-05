'''
Review Python syntax, variables, and data types (integers, floats, strings, lists, dictionaries).
Understand indentation and basic control flow (if statements, loops).
Learn how to use functions and create your own functions.
Explore Python's built-in functions and modules, like print(), input(), len(), range(), and math.

1) Write a Python program to calculate the area of a rectangle ---- DONE 
2) Create a function that takes a list of numbers and returns the sum of all even numbers in the list. --- DONE
3) Write a program that takes user input (their name) and greets them with "Hello, [Name]!".
4)Given a list of integers, write a function to find and return the maximum and minimum values.
5) Write a Python program that swaps the values of two variables without using a temporary variable.
6) Work on a Program that works with Date and Time with the local system. 
'''
## User accepts base & height. Implement formula
## Now do proper
from typing import Union
class Day1_Basics_Service:
    '''
    Write a Python program to calculate the area of a rectangle.
    '''
    ## Type Hinting
    def Area_Triangle(base: Union[int, float], height: Union[int, float]) -> Union[float, int]:
        try:
            if isinstance(base, (int, float)) and isinstance(height, (int, float)):
                area = 0.5 * base * height
                return area
            else: 
                raise TypeError('Value is not a Integer or Float')
        except (Exception, TypeError) as error:
            return error

    ''' 
    Create a function that takes a list of numbers and returns the sum of all even numbers in the list.
    ## Some steps / checks that need to be done.
    validate that the only input is a LIST
    validate that the input is only numbers. 
    '''
    def num_list(num_list: list):
        try:
            if isinstance(num_list, list): 
                check_values = [num for num in num_list if isinstance(num, (int, float))]
                if len(check_values) != len(num_list):
                    raise(TypeError('Values in the list are not all meeting the requirment of Integers and Floats'))
                total = sum(num_list)
                return total
            else:
                raise(TypeError('Input entered is not a list'))
        except (Exception, TypeError) as error:
            return error
        
    #print(num_list(23123))
   # print(num_list([3,4,6,1.23123, '123123']))
    ''' 
    Write a program that takes user input (their name) and greets them with "Hello, [Name]!".
    Start by offering the user what language they would like to speak in. 
    Then Lets take the local date time of the system. and then it will return hello "name" etc.
    '''

    #**TODO Check how to search through dictionarys better
    #**TODO This is a weak point i found
    def request_name():
        print('Choose the corresponding Key with the language requested \nExample Input: (0) to choose English')

        languages = {'0': 'English','1': 'Russian','2': 'Chinese','3': 'Dutch'}
        for key, value in languages.items():
            print(f"{key}, {value}")

        user_input_language = input()
    
        if user_input_language in languages:
            selected_language = {user_input_language: languages[user_input_language]}
            for key, value in selected_language.items():
                user_input_language = value
            return user_input_language
        
        
        else: 
            return False
   
    '''
    4)Given a list of integers, write a function to find and return the maximum and minimum values.
    ## Add error cehcking
    '''

    def list_of_ints(intList: list) -> list:
        ## Step 1: Make sure I am getting a List of integers and nothing more
        ## Step 2: Figure out how to get the min and Max of the integer list. 
        try:
            if isinstance(intList, list):
                check_values = [num for num in intList if isinstance(num, (int))]
                if len(check_values) != len(intList):
                    raise TypeError('Error')
                min_value = min(intList)
                max_value = max(intList)
                return min_value, max_value
        except Exception as error:
            return error

