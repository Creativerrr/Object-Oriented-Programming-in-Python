#Exeptions
#Example 1
class BalanceExeptions(Exception): pass
class Customer:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceEror("Balance has to be non-negative")
        else:
            self.name, self.balance = name, balance
cust = Customer("Larry Torres", -100)