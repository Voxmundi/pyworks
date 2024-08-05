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




class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self,order):
        pass

class DebitPayment(PaymentProcessor):

    def __init(self,security_code):
        self.security_code = security_code


    def pay(self,order,security_code):
        print ("processing debit payment")
        print (f"Verifiying security code {self.security_code}")
        order.status = "paid"

class CreditPayment(PaymentProcessor):

    def __init(self,security_code):
        self.security_code = security_code

    def pay(self,order,security_code):
        print (f"processing credit payment {order.total_price()}")
        print (f"Verifiying security code {self.ecurity_code}")
        order.status = "paid"  

class PaypallPayment(PaymentProcessor):

    def __init(self,email):
        self.email = email

    def pay(self,order,security_code):
        print (f"processing paypall payment {order.total_price()}")
        print (f"Verifiying security code {self.email}")
        order.status = "paid" 


order = Order()

order.add_item("Keyboard", 1, 150)
order.add_item("SSD", 2, 250)
order.add_item("USB", 5, 50)

print(order.total_price())

payment = CreditPayment()

payment.pay(order, "asdas")

print(order.status)






