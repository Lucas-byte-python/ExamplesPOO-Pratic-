# Class Method (Private)------------------------
import datetime

class Account2:
    def __init__(self, number, balance):
        self.__number = number # Attribute Private
        self.__balance = balance # Attribute Private (__balance)

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            self.extract.transaction.append(["SAKE", value, "Date", datetime.datetime.today()])
            return True

def main():
    account = Account2(1, 1000)
    balance = account.balance
    print(balance)

if __name__ == "__main__":
    main()