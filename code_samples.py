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


