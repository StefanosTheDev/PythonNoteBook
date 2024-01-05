## Mutable piece of data is one you can change after you created. 
## Immutable is not able to be changed. 

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1, 
    'Anne': 7
}

another_varaible = friends_last_seen
## ID() is the memory allocation
print(id(friends_last_seen)) 
print(id(another_varaible))