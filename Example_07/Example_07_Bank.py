class Bank:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.accounts = []

    def add_account(self, client_account):
        self.accounts.append(client_account)

    def calculate_monthly_yield(self):
        for account in self.accounts:
            account.calculate_yield()

    def print_account_balances(self):
        for account in self.accounts:
            account.statement()
