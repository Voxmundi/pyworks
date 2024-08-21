

class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.__balance = balance # Private attribute
        self._id = 2
    
    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                raise ValueError("Insufficient Balance")
        else:
            raise ValueError('Withdrawal must be positive')
    
    def __str__(self):
        return f"Account Holder: {self.holder} Balance: {self.__balance}"



account = BankAccount('Alice', 1000)
print (account)
account.deposit(500)
account.withdraw(300)
print (account)
print(account.get_balance())
print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

print(account._id)


