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
# print (Bog.num_dogs())

# print (z)



# z.bark(3) 





"""
1- Good Code should explin  what is it doing 
2- bad code has rigidity: when you modify it, you need to modify tons of others.
that code has dependensies.  Bad depdencies. System are  coupled. 
3- good code is not coupling, o need to work with other related modules. Has minimum depencdeny


"""

# ----------------------- Shallow Copy Deep Copy ------------------
import copy

def s_d_copy():
  a = [1,2,3]
  b = a 

  print (id(a), id(b))

  b.extend([5,6,7])
  print(a)
  print(b)
  # both are changed 


  a = [1,2,3]
  b = a.copy()

  b.extend([5,6,7])
  print(a)
  print(b)

  # b changed a still same but tthis is not deep copy
  # copy() listi deep copy  edeer ama içindeki elemanlar aynı  referansta kalır



  print (id(a[0]), id(b[0])) #same memory  id

  # deepcopy
 


  a = [1,2,3,4,5,[6,7,8]]
  b = copy.deepcopy(a)

  # 2 diffrent id location  
  print (id(a), id(b))

  b[0]= 'hello'
  print(a)
  print(b)

  print (id(a[0]), id(b[0])) #same memory  id


class Pony:
  def __init__(self,name):
    self.name = name

def s_d_classcopy():

  p1 = Pony('vv')
  p2 = copy.copy(p1)

  print(id(p1),id(p2))


# s_d_classcopy()


# ----------------------- Decorator ------------------


def deco_func(original):

  def wrapper(*arg, **kwargs):
    print('executed before {}'.format(original.__name__))
    return original(*arg, **kwargs)
  return wrapper


class Decoratorclass:

  def __init__(self,original):
    self.original = original

  def __call__(self, *args, **kwargs):
    print('call executed before {}'.format(self.original.__name__))
    return self.original(*args, **kwargs)



@deco_func
def display():
  print('display func')


# display()

@Decoratorclass
def get_info(name,age):
  print(name,age)


# get_info('yaman',30)



import logging
import time
from functools import wraps


def my_logger(original):
  logging.basicConfig(filename=f'{original.__name__}.log', level = logging.INFO)

  @wraps(original)
  def wrapper(*args, **kwargs):
    logging.info(
      f'Ran with  args {args} and kwargs {kwargs}'
      )
    return original(*args, **kwargs)

  return wrapper



def my_timer(original):

  @wraps(original)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    result = original(*args, **kwargs)
    t2 = time.time()-t1
    print(f'{original.__name__} ran in {t2} seconds')
    return result 
   

  return wrapper





@my_logger
@my_timer
def display_info(name,age):
  print (name,age)



# display_info('çiço',23)



# ----------------------- lambda ------------------

def lambdax():
  y = lambda x: x+1
  z = lambda x,y: x*y 

  print(y(2))
  print(z(5,7))

  alist = [1,2,3,4,5,6,7,8,9,10]

  def fun1(num):
    return num**2

  squares = map(fun1, alist)
  print(list(squares))

  squares = map(lambda x: x**2, alist)
  print(list(squares))

  even = list(filter(lambda x: x % 2 == 0, alist))
  even = list(filter(lambda x: x > 5, alist))
  print(even)

  blist  = [[1,'a','hello'],[3,'b','world'],[2,'c','ok']]
  sorter = sorted(blist, key=lambda x: x[2])
  print(sorter)

  facy_comp = {x: (lambda x: x**2)(x) for x in range(5)}
  print(facy_comp[2])

# lambdax()




# ----------------------- Iterators  ------------------


a = 'yaman'
b = list(a)
print (b)
c = ''.join(b)
print(c)























