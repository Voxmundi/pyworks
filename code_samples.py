import os


class Employee:

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"My name is {self.name} and I'm {self.age} years old"

  def __repr__(self):
    return f"My name is {self.name} and I'm {self.age} years old"



def os_works():
  print (dir(os))

  print(os.cpu_count())
  print(os.getcwd())
  print(os.listdir())
  print(dir(os.path))
  print(os.environ)


# -----------------------ternary conndition -------------------

def ternary():
  codition = True
  x = 1 if codition else 0 
  print(x) 



# -----------------------enumarate-------------------

def enum():
  names = ['yama', 'ama', 'tamam', 'kahs']
  heros = ['kolo', 'gobo', 'dobo']

  for i,j in enumerate(names,start=1):
    print(i,j)


# enum()

def zipped():
  names = ['yama', 'ama', 'tamam', 'kahs']
  heros = ['kolo', 'gobo', 'dobo']
  for item in zip(names,heros):
    print(item)


# zipped()

# -----------------------upack------------------

def unpack():
  a, b, *c, d = (1,3,3,4,5,6,6)

  print (a)
  print (b)
  print (c)
  print (d)


# unpack()


# ----------------------- getattr - setattr ------------------


class Person:
  pass

person = Person()

def getset():
  person_info = {'first':'yaman', 'last':'ural'}

  for key, value in person_info.items():
   setattr(person, key, value)

  for key in person_info.keys():
    print(getattr(person,key))

# getset()





# ----------------------- LEGB------------------
l = 'Local Scope' 
e = 'Enclosed Scope'
g = 'Global Scope'
b = 'Built in  scope'


from math import e



def legb():
  # be = 5 
  print(e)

e = 3 


# legb()

# ----------------------- Global ------------------


x  = 10 

def glob():
  # global x
  x = 20
  print(x)

  global y
  y = 100

# glob()
# print(x)
# print(y)


# -----------------------Memory Management------------------

x = 300
y = 200+100

# print(x is y)
# print(id(x), id(y))

class Dog:

  def __init__(self,name):
    self.name = name



buddy = Dog('buddy')

# print(buddy.__dict__)




# -----------------------Is  and == ------------------

c = 300
a = 500
b = 1000/2




# print(a is b)

# a = {'name':'banana', 'color':'yelllow'}
# b = {'name':'banana', 'color':'yelllow'}

# print(a == b)




import config
import  sys
import  os


# print(os.__file__)
# print (config.config_version)
# help(os)

# print (sys.path)
sys.path.append('/Users/voxmundi/works/decision')


# ----------------------- Solid ------------------

s = 'Single Resposibilty'
o = 'Open Close Priciple'
l = 'Liskov Substition principle'
i = 'ınterface segregation'
d = 'Dependency inversion'


class Dog():

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def speak (self):
    print(f"Hi I am {self.name} ")

  def talk(self):
    print('Bark')



class Cat(Dog):
 
  def __init__(self,name,age,color):
    super().__init__(name,age)
    self.color = color

  def talk(self):
    print('meeow')




y  = Cat('pisi','5','tekir')
# x = Dog('as',5)
# x.speak()

# y.speak()
# y.talk()


class Bog:

  dogs =[]
  xc = 5 

  def __init__(self,name):
    self.name = name
    self.dogs.append(self)


  @classmethod
  def num_dogs(cls):
    return len(cls.dogs)


  @staticmethod
  def bark(n):
    for _ in range(n):
      print('bark')

  def __str__(self):
    return f'its {self.name}'




z = Bog('zeet')
print (Bog.num_dogs())

print (z)



z.bark(3) 































