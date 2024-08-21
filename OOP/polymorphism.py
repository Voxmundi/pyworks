class Animal:
    def speak(self):
        raise NotImplementedError('subclass will implement')

class Dog(Animal):
    def speak(self):
        return 'Woff'

class Cat(Animal):
    def speak(self):
        return 'Meow'

class Cow(Animal):
    def speak(self):
        return 'Moo'

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.speak())
print(cat.speak())
print(cow.speak())