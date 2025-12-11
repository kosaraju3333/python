class BankAccount:
    def __init__(self,name,balance=0):
        self.account_holder_name=name
        self.balance=balance

    def deposit(self,deposit_amount):
        self.balance=self.balance + deposit_amount
        print(f"Deposited {deposit_amount} to your balance")


    def withdraw(self,withdraw_amount):
        print(f"Your withdrawing....{withdraw_amount} rupees pls wait.............")
        if withdraw_amount > self.balance:
            print(f"Not enough balance!!")
        else:
            self.balance=self.balance-withdraw_amount
            print(f"Successfully withdrew {withdraw_amount}")

    def __str__(self):
        return f"Account Holder Name: {self.account_holder_name}\nBalance: {self.balance}"

obj=BankAccount("Ram")

obj.deposit(2000)
obj.withdraw(5000)

print(obj)