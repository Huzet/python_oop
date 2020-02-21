class User:		
    def __init__(self, username, email_address): 
        self.name = username 
        self.email = email_address 
        self.account_balance = 0 

    def make_deposit(self, amount):
        self.account_balance += amount
        return self	
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def transfer_money(self, other, amount):
        self.account_balance -= amount
        other.make_deposit(amount)
        return self

    def display_account_balance(self):
        print(self.name , self.account_balance)
        return self

tomas = User('Tomas', 'email')
kana = User('Kana', 'email1')
graham = User('Gram', 'email2')

tomas.make_deposit(1000000).make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).display_account_balance()

kana.make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).make_withdrawal(1).display_account_balance()

graham.make_deposit(1000000).make_deposit(1000000).make_withdrawal(1).make_withdrawal(1).display_account_balance()
