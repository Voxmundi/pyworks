from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self,amount):
        pass


class CreditCardPayment(Payment):
    def __init__(self,card_number):
        self.card_number = card_number

    def pay(self, amount):
        print (f"Credit Card payment {amount} from {self.card_number}")



class PaypalPayment(Payment):
    def __init__(self, email):
        self.email = email
    
    def pay(self, amount):
        print (f"Processing PayPall for {amount} from user: {self.email}")


class BitcoinPayment(Payment):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address
    
    def pay(self, amount):
        print (f"Processing Bitcoin for amount {amount} from wallet: {self.wallet_address}")

# client code
def process_payment(payment:Payment, amount):
    payment.pay(amount)


credit_pay = CreditCardPayment('21391-1232-1231')
paypal_pay = PaypalPayment('shd@dhf.com')
bitcoin_pay =  BitcoinPayment('3274328743')

process_payment(credit_pay,100)
process_payment(paypal_pay,100)
process_payment(bitcoin_pay,100)
