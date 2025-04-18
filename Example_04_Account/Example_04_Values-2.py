# Bypassing Private Attributes----------------------
# Python Does Not Have Real Private Attributes------
# Access Can be Obtained----------------------------

from Example_04_Account.Example_04_Account2 import Account2

account = Account2(1, 1000)
balance1 = account._Account2__balance
print(balance1)

# Error Name Incorrect Private----------------------
#balance2 = account.balance
#print(balance2)