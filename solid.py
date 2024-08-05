from abc import ABC, abstractmethod

class Order:
    items =[]
    quantities = []
    prices = []
    status = 'open'

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    
    def total_price(self):
        total = 0 
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total
    

class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self) -> bool:
        pass

class SMSAuth(Authorizer):
    authorized = False

    def verify_code(self,code):
        print(f"Veriying code {code}")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized
    
class NotRobot(Authorizer):
    authorized = False

    def not_robot(self):
        print("You'r not a Robot")
        self.authorized = True
    
    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,order):
        pass

class DebitPayment(PaymentProcessor):

    def __init__(self,security_code, authorizer:Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer


    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception ("Not Authorized")
        
        print ("processing debit payment")
        print (f"Verifiying security code {self.security_code}")
        order.status = "paid"

class CreditPayment(PaymentProcessor):

    def __init__(self,security_code):
        self.security_code = security_code

    def pay(self,order):
        print (f"processing credit payment {order.total_price()}")
        print (f"Verifiying security code {self.security_code}")
        order.status = "paid"  

class PaypallPayment(PaymentProcessor):

    def __init__(self,security_code, authorizer:Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self,order):
        if not self.authorizer.is_authorized():
            raise Exception ("Not Authorized")
        
        print (f"processing paypall payment {order.total_price()}")
        print (f"Verifiying security code {self.email}")
        order.status = "paid" 


order = Order()

order.add_item("Keyboard", 1, 150)
order.add_item("SSD", 2, 250)
order.add_item("USB", 5, 50)
print(order.total_price())


authorizer = NotRobot()
payment = DebitPayment('xxx-eee-2',authorizer)
authorizer.not_robot()
print (payment.security_code)
payment.pay(order)

print(order.status)






