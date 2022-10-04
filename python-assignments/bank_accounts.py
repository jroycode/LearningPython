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
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

invest = BankAccount(.07, 1000000)
savings = BankAccount(.03, 10000)

invest.deposit(150000).deposit(300000).deposit(250000).withdraw(500000).yield_interest().display_account_info()
savings.deposit(50000).deposit(30000).withdraw(10000).withdraw(1000).withdraw(12000).withdraw(500).yield_interest().display_account_info()
