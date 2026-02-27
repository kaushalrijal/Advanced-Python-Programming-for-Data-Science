# write program to generate first n even numbers using iterators

class EvenNumbers:
    def __init__(self, limit):
        self.current = 0
        self.counter = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            self.current += 2
            return self.current
        else:
            raise StopIteration
        
obj = EvenNumbers(15)

for n in obj:
    print(n)
