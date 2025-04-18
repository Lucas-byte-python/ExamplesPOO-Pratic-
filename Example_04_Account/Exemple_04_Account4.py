# New Account------------------------------------------------------------
class Account4:
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
