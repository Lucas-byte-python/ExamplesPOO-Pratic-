# Create One Class -------------------------------------------------------
class Account:
    pass

# Add Method init and self------------------------------------------------
# Self is the way the Class refers to Itself------------------------------
#--init-- is the Constructor Method That Creates the Object of the Class--
class Account:
    def __init__(self, number, cpf, nameHolder, balance):
        self.number = number
        self.cpf = cpf
        self.nameHolder = nameHolder
        self.balance = balance
print()

def main():
    c1 = Account(1, "032.579.148-00", "Lucas", 1000) # Values Add
    print(f"Name the Account Holder: {c1.nameHolder}")
    print(f"Account Number: {c1.number}")
    print(f"Account Holder's CPF: {c1.cpf}")
    print(f"Account Balance: {c1.balance}")

# When a Python script is executed, the reserved variable----------------
# NAME related to it has the value "__main__".---------------------------
# In this case, the condition in the following IF will be TRUE.----------
# So, the code inside the IF block will be executed. In this case,-------
# it is a call to the main method of the script.-------------------------
if __name__ == "__main__":
    main()
print()

#02----------------------------------------------------------------------
class A():
    def f(self):
        print("Full!")

def main():
    obj_A = A() # Object Instance
    obj_A.f()

if __name__ == "__main__":
    main()

# Continue Class Account---------------------------------------------------
class Account:
   def __init__(self, number, cpf, nameHolder, balance):
         self.number = number
         self.cpf = cpf
         self.nameHolder = nameHolder
         self.balance = balance

   def deposit(self, value):
         self.balance += value

   def withdraw(self, value):
         self.balance -= value

   def generate_extract(self):
       print()
       print(f"Number: {self.number} \nCPF: {self.cpf} \nBalance: {self.balance}")

def main():
    c1 = Account(1, 1, "Joao", 0)
    c1.deposit(300)
    c1.withdraw(100)
    c1.generate_extract()

if __name__ == "__main__":
    main()

# Improving the Class---------------------------------------------------------------------
class Account():
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def generate_extract(self):
        print()
        print(f"Number: {self.number} \nCPF: {self.cpf}\nBalance: {self.balance}")

def main():
    c1 = Account(3, "657.321.849-95", "Maria", 0)
    c1.deposit(300)
    sake = c1.withdraw(600)
    c1.generate_extract()
    print(f"Is the Balance Verified? {sake}")

if __name__ == "__main__":
    main()
    print()

#03 Continue -----------------------------------------------------------------------
class Account():
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def sake(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def generate_extract(self):
        print(f"Number:{self.number} \nCPF:{self.cpf}\nBalance:{self.balance}")

    def transferValue(self, depositAccount, value):
        if self.balance < value:
            return ("Insufficient balance!")
        else:
            depositAccount.deposit(value)
            self.balance -= value
            return ("Transaction Performed!")

def main():
    account1 = Account(4, "324.167.895-86", "Clara", 10000)
    value_sake = 2000
    result_sake = account1.sake(value_sake)

    # Validating the return to verify if the withdrawal was completed---------------
    if result_sake:
        print(f"Sake of ${value_sake} Accept Completed!")
        print(f"Balance Actual: ${account1.balance}")
    else:
        print("The Withdrawal was Not Completed - Insufficient Balance!")

if __name__ == "__main__":
    main()
    print()

#04---------------------------------------------------------------------------------
class Account():
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def sake(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def generate_extract(self):
        print(f"Number:{self.number} \nCPF:{self.cpf}\nBalance:{self.balance}")

    def transferValue(self, depositAccount, value):
        if self.balance < value:
            return ("Insufficient balance!")
        else:
            depositAccount.deposit(value)
            self.balance -= value
            return ("Transaction Performed!")

def main():
    account1 = Account(5, "468.357.129-67", 'Kleberiano', 0)
    account2 = Account(6, "648.257.139-56", 'Zezão', 10)

    if (account1 != account2):
        print("Different Memory Addresses")

    print(account1)
    print(account2)

    print(account1.balance)
    print(account2.balance)
    account1.deposit(300)

    print(account1.balance)
    print(account2.balance)

    account1 = account2

    if (account1 == account2):
        print()
        print('Equal Memory Address!')

    print(account1)
    print(account2)

    print(account1.balance)
    print(account2.balance)
    account1.deposit(1000)

    print(account1.balance)
    print(account2.balance)

if __name__ == "__main__":
    main()
    print()
#05------------------------------------------------------------------------
class Account():
    def __init__(self, number, cpf, holderName, balance):
        self.number = number
        self.cpf = cpf
        self.holderName = holderName
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def sake(self, value):
        if self.balance < value:
            return False
        else:
            self.balance -= value
            return True

    def generate_extract(self):
        print(f"Number:{self.number} \nCPF:{self.cpf}\nBalance:{self.balance}")

    def transferValue(self, destinationAccount, value):
        if self.balance < value:
            return ("Insufficient balance!")
        else:
            destinationAccount.deposit(value)
            self.balance -= value
            return ("Transaction Performed!")

def main():
    account1 = Account(10, "324.985.135-00", 'Mendingo', 60)
    account2 = Account(20, "354.987.243-99", 'Japanase', 20000)

    print('Balance Before of the Transfer:')
    print(f"Account Balance One: {account1.balance}")
    print(f"Account Balance Two: {account2.balance}")
    print()

    account1.transferValue(account2, 30)
    print('Balance After of the Transfer:')
    print(f"Account Balance One: {account1.balance}")
    print(f"Account Balance Two: {account2.balance}")

if __name__ == "__main__":
    main()
