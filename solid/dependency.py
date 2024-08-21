import random
import string


# ------------------Without Dependency Inversion Principle

class Order:
    def __init__(self):
        self.id = ''.join(random.choices(string.ascii_lowercase, k=6))
        self.status = 'open'

    def set_status(self, status):
        self.status = status
    

class Authorizer_SMS:
    def __init__(self):
        self.authorized = False
        self.code = None
    
    def generate_sms_code(self):
        self.code = ''.join(random.chocies(string.digits, k=6))
    
    def authorize(self):
        code = input("Enter SMS code")
        self.authorized = code == self.code
    
    def is_authorized(self) -> bool:
        return self.authorized

class PaymentProcessor:

    def pay (self,order):
        authorizer = Authorizer_SMS()
        authorizer.generate_sms_code()
        authorizer.authorize()

        if not authorizer.is_authorized():
            raise Exception ('Not Auhorized')
        
        print(f" processing for order with id {order.id}")
        order.set_status('Paid')






# ------------------With Dependency Inversion Principle


















# ------------------Without Dependency Inversion Principle

class MySqlDatabase:
    def connect(self):
        print("Connecting Database")

    def execute_query(self, query:str):
        print (f"Executing {query}")


class DataProcessor:
    def __init__(self):
        self.db = MySqlDatabase()
    
    def process_data(self):
        self.db.connect()
        self.db.execute_query("SELECT * FROM users")

dt = DataProcessor()
dt.process_data()


from abc import ABC, abstractmethod

class Database(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self,query:str):
        pass

#Mysql Database
class MySqlDatabase(Database):
    def connect(self):
        print ("Connecting Mysql Database")

    def execute_query(self,query:str):
        print (f"Executing query of {query} on Mysql")

#PostgerSql Database
class PostgerSqlDatabase(Database):
    def connect(self):
        print ("Connecting Postger Database")

    def execute_query(self,query:str):
        print (f"Executing query of {query} on PostgerSql")


class DataProcessor:
    def __init__(self, db:Database):
        self.db = db

    def process_data(self,query):
        self.db.connect()
        self.db.execute_query(query)

data_processor = DataProcessor(MySqlDatabase())
data_processor.process_data('yyayaay')






