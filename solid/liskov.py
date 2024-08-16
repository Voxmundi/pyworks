# This adhere LSP 
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height


class Square(Rectangle):

    def __init__(self,side):
        super().__init__(side,side)


def print_area(rect:Rectangle):
    print(f"Area is {rect.area()}")


rect = Rectangle(5,10)
squar = Square(5)

print_area(rect)
print_area(squar)


# violating LSP 
class Square(Rectangle):

    def set_width(self, width):
        self.width = width
        self.height = height #violates LSP 
    


class KıchenModule:

    def on(self):
        return "turned On"
    
    def off(self):
        return "Turned Off"
    
    def set_temparature(self,temp):
        return f"Temperature set to {temp}"

class Toaster(KıchenModule):
    
    def set_temparature(self,temp):
        return f"Toaster Temperature set to {temp}"

class Juicer(KıchenModule):
    pass

t = Toaster()
j = Juicer()

print(t.set_temparature(40))
print(t.on())
print(t.off())

print(j.set_temparature(40))
print(j.on())
print(j.off())




class KıchenModule:

    def on(self):
        return "turned On"
    
    def off(self):
        return "Turned Off"
    
class Heatmodule(KıchenModule):

    def set_temparature(self,temp):
        return f"Toaster Temperature set to {temp}"
    

class Toaster(Heatmodule):
    pass
    
    

class Juicer(KıchenModule):
    pass

t = Toaster()
j = Juicer()

print(t.set_temparature(40))
print(t.on())
print(t.off())

print(j.set_temparature(40))
print(j.on())
print(j.off())




    

    
