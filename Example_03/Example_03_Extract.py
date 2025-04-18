# Compose is a Stronger Form of Association----------------------------
# Where an Object is Part of Another and Cannot Exist Independently----

class Extract:
    def __init__(self):
        self.transaction = [] # Account Transaction List

    def extract(self, numberAccount):
        print(f"Extract: {numberAccount}\n")

        for transaction in self.transaction:
            print(f"{transaction[0]:15s} {transaction[1]:10.2f} {transaction[2]:10s} {transaction[3].strftime('%d/%b/%Y')}")