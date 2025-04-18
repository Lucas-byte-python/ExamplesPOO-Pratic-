# Account Class Added to Customer Class----------------------------
class Account:
    def __init__(self, customers, number, balance):
        self.customers = customers
        self.number = number
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True
    def transferValue(self, destinationAccount, value):
        if self.balance < value:
            return ("Insufficient Balance!")
        else:
            destinationAccount.deposit(value)
            self.balance -= value
            return ("Transfer Completed!")

    def generateBalance(self):
        print(f'Number:{self.number} '
              f'\nBalance:{self.balance}')