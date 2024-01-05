## Generators function: Remembers the state it's in between executions. 
def hundred_numbers():
    i = 0
    while i < 100: 
        yield i # Gives you I when u call it . Then it remembers. YIELD is critical.
        i += 1
g = hundred_numbers()
print(next(g)) ## Next is a built in function that affects generators. Means go up to the Yield.
print(next(g))


#my_range_obj = range(10)  # Range object is not quite a Iterator. 
#print(my_range_obj) # the output is essentially similar to the __repr__())


print(list(g)) ## Starts from 2 not from 0 