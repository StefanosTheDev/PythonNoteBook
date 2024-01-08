
'''
** Counter
* Defaultdict
* ordereddict
*namedtuple
*deque
'''
'''
from collections import Counter

device_temperatures = [13.5, 14.0, 14.0, 14.5, 14.5, 14.5, 15.0, 16.0]

temperature_counter = Counter(device_temperatures)
print(temperature_counter[14.5])

print(Counter({'hello': 5, 'hi': 3})['hi']) ### Another way we can do this.
'''


from collections import defaultdict

coworkers = [('Rolf', 'MIT'),('Jen', 'Oxford'),('Rolf', 'Cambridge'),('Charlie', 'Manchester')]

alma_matters = defaultdict(list) ## list() User()
for coworker in coworkers:
    if coworker[0] not in alma_matters:
        alma_matters[coworker[0]] = []
    alma_matters[coworker[0]].append(coworker[1])

{
    'Rolf': ['MIT, Cambridge'],
    'Jen': ['Oxford'],
    'Charlie': ['Manchester']
}

#alma_matters.default_factory = None # Remove the default []. So you would get an error if you want to check empty.  This way we wont returnaempty lists. 

alma_matters.default_factory = int ## this would print back a 0. So you could check that as well. 
print(alma_matters['Rolf']) ## ['MIT', 'Cambridge'] 
print(alma_matters['Anne']) ## [] 


alma_matters.default_factory = None


####################Default Dict

my_company = 'Teclado'
coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]
coworker_companies = {'Jen': 'Teclado', 'Rolf': 'Apple Inc.'}

coworker_companies = defaultdict(lambda: my_company)  ## default dict takes in a fucntion so we need the lambda 

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworkers[0]])
print(coworker_companies['Rolf'])



''' 
Ordered Dict


from collections import OrderedDict  ##Dictionaries i think keep there order 
o = OrderedDict() ## Ordered in the way they were inserted. 
o['Rolf'] = 6
o['Jose'] = 12
o['Jen'] = 3
print(o)
o.move_to_end('Rolf')
o.move_to_end('Jose', last=False)
print(o)

o.popitem() #Remove item fromthe end. 
print(o)
'''
'''
from collections import namedtuple

account = ('checking', 1850.90)
#print(account[0]) # name
#print(account[1]) # balance

Account = namedtuple('Account', ['name','balance']) ## make sure that the format is like this with the variable. 
account = Account('checking', 1850.90)
print(account.name)
print(account)

'''
'''
from collections import deque ## we use it sometimes more than a list because its thread safe usefull when dealing with threads

friends = deque(('Rolf', 'Charlie', 'Jen', 'Anna'))
friends.append('Jose')
friends.appendleft('Anthony')

print(friends)
friends.pop() #on the end of the right side
friends.popleft() # on the left side

print(friends)
'''


def task1() -> defaultdict:
    def_obj = defaultdict(lambda: 'Unknown')
    def_obj['Alen'] = 'Manchester'
    return def_obj
print(task1())



def task2(arg_od: OrderedDict):
    """
    - takes in an OrderedDict `arg_od`
    - Remove the first and last entry in `arg_od`.
    - Move the entry with key name `Bob` to the end of `arg_od`.
    - Move the entry with key name `Dan` to the start of `arg_od`.
    - You may assume that `arg_od` would always contain the keys `Bob` and `Dan`,
        and they won't be the first or last entry initially.
    """
    # you code starts here:
    pass


def task3(name: str, club: str) -> namedtuple:
    """
    - create a `namedtuple` with type `Player`, and it will have two fields, `name` and `club`.
    - create a `Player` `namedtuple` instance that has the `name` and `club` field set by the given arguments.
    - return the `Player` `namedtuple` instance you created.
    """
    # you code starts here:
    pass


def task4(arg_deque: deque):
    """
    - Manipulate the `arg_deque` in any order you preferred to achieve the following effect:
        -- remove last element in `deque`
        -- move the fist (left most) element to the end (right most)
        -- add an element `Zack`, a string, to the start (left)
    """
    # you code starts here:
    pass