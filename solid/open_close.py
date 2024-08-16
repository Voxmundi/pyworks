from abc import ABC, abstractmethod

# -------------------inheritance 
class Shape: 
    def draw(self):
        raise NotImplementedError
    
class Circle(Shape):
     
     def draw(self):
         return 'Draiwing Circle'

class Square(Shape):

    def draw(self):
        return 'Drawing Square'
    

# -------------------interface



class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def draw(self):
        return "Drawing Circle"

    def area(self):
        return 5
    

class Square(Shape):

    def draw(self):
        return 'Drawing Square'

# -------------------composition

class Renderer:
    def render(self,shape):
        return f"rendering {shape.draw()}"

class Shape:
    def draw(self):
        return "some shape"
    
class Circle(Shape):
    def draw(self):
        return "Draving circle"

circle = Circle()
renderer = Renderer()

print(renderer.render(circle))



class DiscountCalculator:

    def calculate (sef,price,discount_type):
        if discount_type == 'percent':
            return price*0.9
        elif discount_type == 'fixed':
            return price-10


class DiscountStrategy(ABC):

    @abstractmethod
    def apply_discount(self,price):
        pass

class PercentDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price*0.9

class FixedDiscount(DiscountStrategy):

    def apply_discount(self, price):
        return price-10
    
class DicountCalculator:

    def calculate(self,price, strategy:DiscountStrategy):
        return strategy.apply_discount(price)


a = DicountCalculator()

print (a.calculate(80,PercentDiscount()))
print (a.calculate(80,FixedDiscount()))



class PaymentProcessor(ABC):
    @abstractmethod
    def payment_process(self,amount:float):
        pass

class CreditPayment(PaymentProcessor):
    def payment_process(self, amount: float):
        return f"Credit payment process"
    
class PaypalPayment(PaymentProcessor):
    def payment_process(self, amount: float):
        return f"Paypall payment process"

class BitcoinPayment(PaymentProcessor):
    def payment_process(self, amount: float):
        return f"Bitcoin payment process"


def process_payment(processor:PaymentProcessor,amount:float):
    print(processor.payment_process(amount))


# Example usage
credit_card = CreditPayment()
paypal = PaypalPayment()
bitcoin = BitcoinPayment()

process_payment(credit_card, 100.0)
process_payment(paypal, 200.0)
process_payment(bitcoin, 300.0)    

class ApplePay(PaymentProcessor):
    
    def payment_process(self, amount: float):
        return "Processing Apple payment {amount}"
    
apple_pay = ApplePay()
process_payment = (apple_pay,500)






