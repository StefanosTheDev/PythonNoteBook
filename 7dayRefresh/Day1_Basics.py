'''
Review Python syntax, variables, and data types (integers, floats, strings, lists, dictionaries).
Understand indentation and basic control flow (if statements, loops).
Learn how to use functions and create your own functions.
Explore Python's built-in functions and modules, like print(), input(), len(), range(), and math.

1) Write a Python program to calculate the area of a rectangle ---- DONE 
2) Create a function that takes a list of numbers and returns the sum of all even numbers in the list. --- DONE
3) Write a program that takes user input (their name) and greets them with "Hello, [Name]!".
Given a list of integers, write a function to find and return the maximum and minimum values.
Write a Python program that swaps the values of two variables without using a temporary variable.

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
        
    print(num_list(23123))
   # print(num_list([3,4,6,1.23123, '123123']))
    ''' 
    Write a program that takes user input (their name) and greets them with "Hello, [Name]!".
    '''
    def request_name():
        pass
    