# Using the @property Decorator, We Can Protect Attributes---
# And Acess Only throught of Method "Decorated"--------------
class Account3:
    def __init__(self, number):
        self.number = number
        self._balance = 0

    @property  # Method Decorated
    def balance(self):
        return self._balance

    @balance.setter  # Alter to Balance - Method Setter
    def balance(self, balance):
        if balance < 0:
            print("Balance Invalid")
        else:
            self._balance = balance

def main():
    account = Account3(1)
    account.balance = 1000 # Balance.Setter
    print(f"Balance Account = {account.balance}") # @property

if __name__ == "__main__":
    main()