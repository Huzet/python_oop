class User:		
    def __init__(self, username, email_address): 
        self.name = username 
        self.email = email_address 
        self.account_balance = 0 

    def make_deposit(self, amount):
        self.account_balance += amount	
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other, amount):
        self.account_balance -= amount
        other.make_deposit(amount)

    
        
    		
tomas = User('Tomas', 'email')
kana = User('Kana', 'email1')
graham = User('Gram', 'email2')
tomas.make_deposit(1000000)
tomas.make_deposit(1000000)
tomas.make_deposit(1000000)
tomas.make_withdrawal(1)

kana.make_deposit(1000000)
kana.make_deposit(1000000)
kana.make_withdrawal(1)
kana.make_withdrawal(1)

graham.make_deposit(1000000)
graham.make_deposit(1000000)
graham.make_withdrawal(1)
graham.make_withdrawal(1)

tomas.transfer_money(graham, 1)

print(tomas.account_balance)
print(graham.account_balance)
