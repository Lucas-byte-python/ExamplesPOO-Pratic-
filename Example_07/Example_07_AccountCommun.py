from Example_07_AccountCustomer import ClientAccount

class RegularAccount(ClientAccount):
    def __init__(self, number, IOF, IR, invested_amount, yield_rate):
        super().__init__(number, IOF, IR, invested_amount, yield_rate)

    def calculate_yield(self):  # (2)
        remuneration = self.invested_amount * self.yield_rate
        iof_amount = remuneration * self.IOF
        self.invested_amount += remuneration - iof_amount