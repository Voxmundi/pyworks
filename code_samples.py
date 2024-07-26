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



getset()














