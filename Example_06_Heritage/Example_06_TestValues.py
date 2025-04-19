# Heritage Class---------------------------------------------------------------
from Example_03.Example_03_Customer import Customer
from Example_03.Example_03_Account_Customer_Extract import Account
from Example_06_Heritage.Example_06_AccountSpecial import AccountSpecial

# Values
customer1 = Customer(321, "Lucas", "Road X")
customer2 = Customer(132, "Maria", "Road II")
customer3 = Customer(231, "Luiza", "Road H")

# The Three Accounts Started, the Common Accounts With a Balance of 2000 and the Special Account With a Balance of 1000 and a Limit of 2000
account1 = Account(customer2,  1, 2000)
account2 = Account(customer2,  2, 2000)
account3 = AccountSpecial(customer3,  3, 1000, 2000)

# Print the Balance of Three Account
print(f'Customer: {customer1.cpf} of Account Common {account1.number} can Balance R$ {account1.balance}')
print(f'Customer: {customer2.cpf} of Account Common {account2.number} can Balance R$ {account2.balance}')
print(f'Customer: {customer3.cpf} of Account Special {account3.number} can Balance R$ {account3.balance} and Limit Account R$ {account3.limit}\n')

# Deposit 500 and Sake 3000 of Account Common, and Not Balance
account2.deposit(500)

# Massage Indicating Balance After Deposit
print(f"Customer: {customer2.cpf} of Account Common {account2.number} can Balance R$ {account2.balance} \n")

account2.withdraw(3000)

# Massage Can´t Sake Balance Again
print(f"Customer: {customer2.cpf} of Account Common {account2.number} can´t Balance R$ {account2.balance} \n")

# Deposit 100 and Again Sake 2000 of Account Special With Limit
account3.deposit(100)

# Massage Indicate Balance After Deposit
print(f"Customer: {customer3.cpf} of Account Special {account3.number} can Balance R$ {account3.balance} and Limit {account3.limit} \n")

account3.withdraw(2000)

# Massage Indicate Can´t Sake Balance Negative
print(f"Customer: {customer3.cpf} of Account Special {account3.number} can Balance R$ {account3.balance} and Limit {account3.limit} \n")

# Attempted Withdrawal Above the Limit
account3.withdraw(2000)
print(f"Customer: {customer3.cpf} of Account Common {account3.number} can Balance R$ {account3.balance} and Limit R$ {account3.limit} \n")
