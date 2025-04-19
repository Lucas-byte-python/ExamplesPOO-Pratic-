class ClientAccount:
    def __init__(self, number, IOF, IR, invested_amount, yield_rate):
        self.number = number
        self.IOF = IOF
        self.IR = IR
        self.invested_amount = invested_amount
        self.yield_rate = yield_rate

    def calculate_yield(self):
        remuneration = self.invested_amount * self.yield_rate
        iof_amount = remuneration * self.IOF
        ir_amount = remuneration * self.IR
        self.invested_amount += remuneration - iof_amount - ir_amount

    def statement(self):  # (1)
        print(f"The current balance of account {self.number} is {self.invested_amount:10.2f}")
