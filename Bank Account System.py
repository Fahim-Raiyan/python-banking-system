class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        print(f"Balance before deposit: Tk. {self.__balance}")
        if amount>0:
            self.__balance+=amount
            print(f"Balance after deposit: Tk. {int(self.__balance)}") 
        else:
            print("The deposited amount cannot be 0 or negative!")
    def withdraw(self,amount):
        print(f"Balance before withdrawal: Tk. {int(self.__balance)}")
        if amount>0 and amount <= self.__balance:
            self.__balance-=amount
            print(f"Balance after withdrawal: Tk. {int(self.__balance)}")               
        elif amount<0:
            print(f"Withdrawn amount Tk. {amount} is less than 0. Try Again!")
        elif amount > self.__balance:
            print(f"Your withdrawal value Tk. {amount} is more than the existing balance. Try Again!")
    def get_bal(self):
        return self.__balance
    def update(self,n_bal):
        self.__balance=n_bal
class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.__intrate=rate
        print(f"Account created: Savings Account for {self.owner}")
    def interest(self):
        balance=self.get_bal()   
        interest=balance * self.__intrate
        self.deposit(interest)
        print(f"Interest applied: New Balance = Tk. {int(self.get_bal())}")
    def withdraw(self, amount):
        balance=self.get_bal()
        if amount > balance:
            print("Insufficient funds - Overdraft not allowed!")
        else:
            super().withdraw(amount)

class CheckingAccount(Account):
    def __init__(self, owner, balance,odlim):
        super().__init__(owner, balance)
        self.__oli=odlim
        print(f"Account created: Checking Account for {self.owner}")
    def withdraw(self, amount):
        balance=self.get_bal()
        print(f"Balance before withdrawal: Tk. {int(balance)}")
        if amount <= balance:
            n_bal=balance-amount
            self.update(n_bal)
            print(f"Balance after withdrawal: Tk. {int(balance-amount)}")
        elif amount > balance and amount <= balance + self.__oli:
            n_bal=balance-amount
            self.update(n_bal)
            print("Overdraft protection applied: Withdrawal allowed")
            print(f"Balance after withdrawal: Tk. {int(balance-amount)}")
        elif amount > balance + self.__oli:
            print("Withdrawal denied! Exceeds overdraft limit!")

s=SavingsAccount("Fahim",45000,0.05)
s.deposit(5000)
s.withdraw(2500)
s.interest()
s.withdraw(10000)
print(f"Final Balance= Tk. {int(s.get_bal())}")
print("\n")
c=CheckingAccount("Rahim",64000,5000)
c.deposit(4000)
c.withdraw(15000)
print(f"Final Balance= Tk. {int(c.get_bal())}")


        
            


