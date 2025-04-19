from Example_03.Example_03_Account_Customer_Extract import Account
import datetime

class AccountSpecial(Account):
    def __init__(self, custumers, number, balance, limit):
        super().__init__(custumers, number, balance) # Heritage Attributes of Super Class (Account)--Custumers--Number--Balance
        self.limit = limit

    def withdraw(self, value):
        if (self.balance + self.limit) < value:
            print(f"Not Exist Balance Enough Account Number {self.number} Customer {self.customers.cpf}")
            return False
        else:
            self.balance -= value
            if (self.balance < 0):
                self.limit += self.balance
            self.extract.transaction.append(["SAKE", value, datetime.datetime.today()])
            return True

    # Method Rewritten for Account Special
    def deposit(self, value):
        pass