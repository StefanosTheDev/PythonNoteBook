class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self): ## All generators are Iterators. You can have iterators that dont generate numbres
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration() # Reached end of Generator
my_gen = FirstHundredGenerator()
print(next(my_gen))
print(next(my_gen))

## NOt all iterators have to be generators
class FirstHundredIterator:
    def __init__(self):
        self.numbers = [1,2,3,4,5]
        self.i = 0

    def __next__(self):
        if self.i < len(self.numbers):
            return self.numbers[self.i]
        else: 
            raise StopIteration()