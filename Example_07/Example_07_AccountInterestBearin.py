from Example_07_AccountCustomer import ClientAccount

class InterestBearingAccount(ClientAccount):
    def __init__(self, number, IOF, IR, invested_amount, yield_rate):
        super().__init__(number, IOF, IR, invested_amount, yield_rate)

    def calculate_yield(self):  # (3)
        self.invested_amount += self.invested_amount * self.yield_rate