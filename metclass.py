class Foo:
    
    def hi(self):
        return 'hi'

def hello(self):
    return 'Hello'

print(type(Foo))

# type(classname, baseclass, attr)
# type('Name',(),{})

Test = type('Test',(Foo,),{'x':5,'hello':hello})

y = Test()
print(y.hello())
print(y.x)
print(y.hi())


class Private(type):
    def __new__(self,class_name,bases, attr):
        
        print(attr)
        a = {}
        for item in attr.keys():
            if item.startswith('__'):
                a[item] = attr[item]
            else:
                a['__'+item] = attr[item]
        print(a)

        return type(class_name,bases,a)


class SomeClass(metaclass=Private):
    x = 5
    y = 9
    z = 10

    def hello(self):
        print ('hi')

y = SomeClass()
y.__hello()
print(y.__z)





class MyMeta(type):

    def __new__(self,name,bases,attr):
        print (f"Creating a new class named {name}")
        attr['__id'] = 5
        return super().__new__(self,name,bases,attr)

class Myclass(metaclass = MyMeta):
    n = 5
    def __init__(self,x):
        self.x = x



obj = Myclass(3)
print (obj.n)
print (obj.__id)

class SingletonMeta(type):
    _instances = {}

    def __call__(cls,*args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances

class Singleton(metaclass =SingletonMeta):
    
    def __init__(self):
        print('Singleton Created')


s1 = Singleton()
s2 = Singleton()

print (s1 is s2)



















