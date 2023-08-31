numbers = [0,1,2,3,4]
double_numbers = []

double_num = [num * 2 for num in numbers]
print(double_num)

friends_ages = [12,31,35,37]
age_strings = [f" My friends is {age} years old" for age in friends_ages] ## another way to do list comprehension
print(age_strings)

names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)


odds = [age for age in friends_ages if age % 2  == 1]
print(odds)

