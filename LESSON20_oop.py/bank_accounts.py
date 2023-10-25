class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")
        
    def getBalance(self):
        print(f"Account '{self.name}' balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}") 
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
            
    # Transaction from one account to another
    def transfer(self, amount, account):
        try:
            print("\n**********\nBeginning Transfer.. 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Tranfer complete! ✅\n**********")
        except BalanceException as error:
            print(f"Tranfer interrupted. ❌{error}\n**********")
       
class InterestRewardAcct(BankAccount):
    # received 5% for all deposit
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("Deposit complete.")
        self.getBalance()
    
class SavingAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        # fee = frais
        self.fee =  5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdraw interrupted. ❌")
            
    
    