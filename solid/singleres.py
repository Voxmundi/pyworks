
class UserManager:

    def __init__(self,user_data):
        self.user_data  = user_data
    
    def save_to_database(self):
        print (f"Saving user data to database {self.user_data}")
    
    def send_welcome_mail(self):
        print (f"Sending welcome mail to {self.user_data['email']} ")
    
    def generate_report(self):
        print (f"Generating report for {self.user_data['name']} ")
    


class User:

    def __init__(self, name,surname, email):
        self.name = name
        self.surname = surname
        self.email = email

class UserRepesitory:

    def save(self, user:User):
        print(f"Saving user: {user.name} to database")

class EmailService:

    def send_email(self,user:User):
        print (f"Sending email to user {user.email}")

class ReportProcess:

    def generate_report(self,user:User):
        print (f"Generating Report for {user.name} {user.surname}")

        





