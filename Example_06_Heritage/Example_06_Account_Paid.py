# Heritage Paid Account-----------------------------------------------------------
from Example_03.Example_03_Account_Customer_Extract import Account
from Example_06_Heritage.Example_06_Saving import Saving

class AccountPaidSaving(Account, Saving):
    def __init__(self, rate_paid, customers, number, balance):
        Account.__init__(self, customers, number, balance)
        Saving.__init__(self, rate_paid)

    def paidAccount(self):
        self.balance += self.balance * (self.rate_paid_month / 30)