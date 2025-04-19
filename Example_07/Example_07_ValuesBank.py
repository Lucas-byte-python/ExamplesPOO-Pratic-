# Test Polymorphism
from Example_07.Example_07_AccountCommun import RegularAccount
from Example_07_AccountCustomer import ClientAccount
from Example_07_Bank import Bank
from Example_07_AccountCommun import ClientAccount
from Example_07_AccountInterestBearin import InterestBearingAccount

bank1 = Bank(999, "test")
client_account1 = ClientAccount(1, 0.01, 0.1, 1000, 0.05)
regular_account1 = RegularAccount(2, 0.01, 0.1, 2000, 0.05)
interest_bearing_account1 = InterestBearingAccount(3, 0.01, 0.1, 2000, 0.05)

bank1.add_account(client_account1)     # (4)
bank1.add_account(regular_account1)    # (5)
bank1.add_account(interest_bearing_account1)  # (6)
bank1.calculate_monthly_yield()        # (7)
bank1.print_account_balances()         # (8)