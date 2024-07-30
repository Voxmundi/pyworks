

class Employee():

	raise_amount = 1.04
	num_emloyees = 0 

	def __init__(self,first, last, payment):
		self.first = first
		self.last = last
		self.payment = payment
		

		Employee.num_emloyees +=1

	@property
	def email (self):
		return f"{self.first}.{self.last}@compay.com"


	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.payment = int(self.payment * Employee.raise_amount)

	@classmethod
	def set_raise(cls,amount):
		cls.raise_amount = amount

	@classmethod
	def from_string(cls,emp_str):
		first, last, payment = emp_str.split('-')
		return cls(first, last, payment)

	@staticmethod
	def is_working(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True 

	def __repr__(self):
		return (f"Employe {self.first}.{self.last} = {self.payment}" )

	def __str__(self):
		return (f"Employe ({self.first},{self.last},{self.payment})" )

class Developer(Employee):
	raise_amount = 1.05

	def __init__(self,first, last, payment, prog_lang):
		super().__init__(first, last, payment)
		self.prog_lang = prog_lang

class Manager(Employee):

	def __init__(self, first, last, payment,employees=None):
		super().__init__(first, last, payment)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self,emp):

		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):

		if emp in self.employees:
			employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print('--->', emp.fullname())

def oop5():
	emp3 = Manager('çiço', 'ipoo', 5000)
	emp2 = Developer('çido', 'pipoo', 3000, 'Python')
	emp1 = Employee('çiço', 'ipoo', 5000)

	print(emp1)
	print(emp1.__repr__())
	print(emp2.__str__())

	a = [1,4,5,6,7,5]

	print(a.__len__())
	
def oop4():
	emp1 = Manager('çiço', 'ipoo', 5000)
	emp2 = Developer('çido', 'pipoo', 3000, 'Python')
	emp1.add_employee(emp2)
	print(emp1.__dict__)
	emp1.print_emp()

	print(isinstance(emp1, Manager) )
	print(isinstance(emp2, Employee) )


	print(issubclass(Developer,Developer))
	print(issubclass(Developer,Manager))
	print(issubclass(Developer,Employee))

def oop3():
	emp1 = Employee('çiço', 'ipoo', 5000)
	emp2 = Developer('çido', 'pipoo', 3000, 'Python')
	print(emp1.raise_amount)
	print(emp2.raise_amount)
	print(emp2.prog_lang)

def opp2():
	emp1 = Employee('çiço','ipoo',5000)
	emp2 = Employee('çido','pipoo',3000)

	print(emp1.raise_amount)
	emp1.set_raise(1.05)
	print(emp1.raise_amount)
	print(emp2.raise_amount)

	emp_str = 'Yaman-Ural-8000'

	emp3 = Employee.from_string(emp_str)
	print(emp3.payment)
	print(Employee.num_emloyees)

	import datetime
	my_date = datetime.date(2024,7,28)
	print (Employee.is_working(my_date))

def oop_1():

	print (Employee.num_emloyees)

	emp1 = Employee('yamn','ural', 3000)
	print(emp1.__dict__)

	print(emp1.fullname())

	print(emp1.payment)
	emp1.apply_raise()
	print(emp1.payment)

	print (Employee.num_emloyees)





class Empl():

	raise_amount = 1.04
	num_emloyees = 0 

	def __init__(self,first, last, payment):
		self.first = first
		self.last = last
		self.payment = payment
		Employee.num_emloyees +=1

	@property
	def email (self):
		return f"{self.first}.{self.last}@compay.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"

	@fullname.setter
	def fullname(self,name):
		first, last = name.split(' ')
		self.first = first
		self.last = last



def oop6():

	emp1 = Employee('yamn','ural', 3000)
	# emp1.first = 'grgr'
	emp1.fullname = 'Yaman Ural'

	print(emp1.email)
	print(emp1.fullname)




oop6()
