

class Person:

    def __init__(self, name, last, age):
        self.name = name
        self.last = last
        self.age = age
        self.employe = []
        self.team = 'BJK'

person = Person('yaman', 'Ural', 48)
print(person.name)
print(person.last)
print(person.age)
print(person.team)
print(person.employe)

class Vehicle:
    def __init__(self, type_of):
        self.type = type_of


class Car(Vehicle):

    def __init__(self, make, model, year):
        super().__init__('Car')
        self.make = make
        self.model = model
        self.year = year
mycar = Car('Toyota', 'Corolla', 2020)

print (mycar.type)