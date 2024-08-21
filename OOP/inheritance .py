class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def make_sound (self):
        return f"{self.name} make a sound"
    
    def info (self):
        return f"{self.name} is a {self.species}"


class Dog (Animal):

    def __init__(self, name, breed ):
        # Calling the constructor of the Parent class
        super().__init__(name, species = 'Dog')
        self.breed = breed
        
    # Overriding the make_sound method
    def make_sound(self):
        return f"{self.name} barks "
    
    def dog_info(self):
        return f"{self.name} is a {self.breed}"
    
class Cat(Animal):

    def __init__(self,name,color):
        super().__init__(name, species='Cat')
        self.color = color
    
    def make_sound(self):
        return f"{self.name} sound meow"
    
    def cat_info(self):
        return f"{self.name} is a {self.color} Cat"


dog = Dog("buddy", "Retriever")
cat = Cat("Mişa", "Colorfull")

print (dog.info())
print(cat.info())

print (dog.make_sound())
print(cat.make_sound())

print (dog.dog_info())
print(cat.cat_info())






    