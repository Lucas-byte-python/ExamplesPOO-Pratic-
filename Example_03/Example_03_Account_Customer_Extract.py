# Composition is a stronger form of Association----------------------------
# Where one Object is Part of Another and Cannot Exist Independently-------
import datetime
from Example_03.Example_03_Extract import Extract

class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance
        self.date_openning = datetime.datetime.today()
        self.extract = Extract() # Init The Compose

    def deposit(self, value):
        self.balance += value
        self.extract.transaction.append(["DEPOSIT", value, "Date", datetime.datetime.today()])

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            self.extract.transaction.append(["SAKE", value, "Date", datetime.datetime.today()])
            return True

    def tranferValue(self, accountDestination, value):
        if self.balance < value:
            return ("Insufficient Balance")
        else:
            accountDestination.deposit(value)
            self.balance -= value
            self.extract.transaction.append(["TRANSFER", value, "Date", datetime.datetime.today()])
            return ("Transfer Completed")

    def generate_balance(self):
        print(f"Number: {self.number}\nBalance: {self.balance}")