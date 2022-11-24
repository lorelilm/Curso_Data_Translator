#Create class
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        return f"woof! my name is {self.name}"

#Multiple objects
dogs = []
for name in ['fido', 'lassy', 'milo']:
    d = Dog(name)
    dogs.append(d)

for i, d in enumerate(dogs):
    print(f"dog {i} barking {d.bark()}")