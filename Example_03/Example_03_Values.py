# Perform Aggregation-------------------------------------------------------

from Example_03.Example_03_Customer import Customer
from Example_03.Example_03_Account_Customer_Extract import Account

customer1 = Customer(321, "Lucas", "Road X")
customer2 = Customer(132, "Maria", "Road II")

# Creat One Account with Two Customers, Performing Aggregation with a List--
account1 = Account([customer1, customer2], 2, 3000)

account1.deposit(2000)
account1.withdraw(500)
account1.extract.extract(account1.number)
