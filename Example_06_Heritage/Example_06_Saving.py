# Class Saving--------------------------------------------------
import datetime

class Saving:
    def __init__(self, ratePaid):
        self.rate_paid_month = ratePaid
        self.date_init = datetime.datetime.today()

    def paidAccount(self):
        self.balance += self.balance * self.rate_paid_month