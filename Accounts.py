class Account:
    def __init__(self,name,balance):
        self.name = name 
        self.balance = balance 
    
class SavingAccount(Account):
    def __init__(self,name,balance,interest_rate):
        super().__init__(name,balance)
        self.interest_rate = interest_rate 

class PremiumAccount(SavingAccount):
    def __init__(self,name,balance,interest_rate,cashback):
        super().__init__(name,balance,interest_rate)
        self.cashback = cashback 
    
    def display(self):
        print(f"Account: {self.name}")
        print(f"Balance: rs{self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Cashback: {self.cashback}")

account1 = PremiumAccount("Vishakha",50000,4.5,"Enabled")
account1.display()
