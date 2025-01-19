# 63. Encapsulation
class Account:
    def __init__(self):
        self._balance = 0
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
        else:
            print("Invalid balance amount.")

account = Account()
account.set_balance(100)
print("Balance:", account.get_balance())