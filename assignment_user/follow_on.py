class User:
    def __init__(self, username, email_address): 
        self.name = username 
        self.email = email_address 
        self.account = bank_account()

    def make_deposit(self, amount):
        self.account.deposit(amount)	
        return self	

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def transfer_money(self, other, amount):
        self.account -= amount
        other.make_deposit(amount)
        return self


class bank_account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.int_rate = 0.01

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self


# ASSIGNMENT BANK ACCOUNT
# tomas_bankaccount = bank_account('richie', 1000000, 0.01)
# kana_bankaccount = bank_account('bankie', 1000000, 0.01)
# kana_bankaccount.deposit(1).deposit(1).deposit(1).withdraw(1).display_account_info()
# # kana_bankaccount.deposit(1).deposit(1).deposit(1).withdraw(1).display_account_info()
# tomas_bankaccount.deposit(1).deposit(1).withdraw(1).withdraw(1).withdraw(1).withdraw(1).yield_interest().display_account_info()

# ASSIGNMT CHAINING METHODS
# tomas = User('Tomas', 'email')
# kana = User('Kana', 'email1')
# graham = User('Gram', 'email2')
# tomas.make_deposit(1000000).make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).display_account_balance()
# kana.make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).make_withdrawal(1).display_account_balance()
# graham.make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).make_withdrawal(1).display_account_balance()
