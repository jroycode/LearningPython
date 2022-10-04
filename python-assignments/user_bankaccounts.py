class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance = self.balance - amount
        
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance = self.balance - 5
        return self

    def display_account_info(self):
        return f"Balance: {self.balance}"

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name
        self.account = {
            "investing" : BankAccount(.07,1000000),
            "checking" : BankAccount(.03, 30000)
        }

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.account.display_account_info()}")
        return self

    def transfer(self,amount,user):
        self.amount = self.amount - amount
        user.amount = user.amount + amount
        self.display_user_balance()
        user.display_user_balance()
        return self