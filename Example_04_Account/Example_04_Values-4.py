# Class Account-------------------------------------------------------------
from Example_04_Account.Exemple_04_Account4 import Account4

def main():
    account = Account4(1)
    account.balance = 1000 # Balance.Setter
    print(f"Balance Account = {account.balance}") # @property

if __name__ == "__main__":
    main()