
class Account:
    def __init__(self,accout_holder):
        self.balance=0
        self.holder=accout_holder
        
    def deposit(self,amout):
        self.balance+=amout
        return self.balance
    
    def withdraw(self,amout):
        if self.balance>=amout:
            self.balance-=amout 
            return self.balance
        else:
            return 'Insufficient funds'