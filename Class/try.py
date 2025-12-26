class Animal:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Animal name is {self.name}"
    
    def __repr__(self):
        return f"Animal : {self.name}"

    def sayHello(self):
        print(f"{self.name} says Meow!")

a1 = Animal("pussy")
a1.sayHello()

a1