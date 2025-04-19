# Account Savings -- Multiples Heritage-----------------------------------------------
from Example_03.Example_03_Customer import Customer
from Example_03.Example_03_Account_Customer_Extract import Account
from Example_06_Heritage.Example_06_Account_Paid import AccountPaidSaving
from Example_06_Heritage.Example_06_Saving import Saving


customer1 = Customer("123", "Lucas", "Rua X")
customer2 = Customer("456", "Maria", "Rua W")

account1 = Account([customer1, customer2], 1, 2000)
account_saving1 = Saving(0.1)
account_paid1 = AccountPaidSaving(0.1, [customer1], 5, 1000)

account_paid1.paidAccount()
account_paid1.generate_balance()

