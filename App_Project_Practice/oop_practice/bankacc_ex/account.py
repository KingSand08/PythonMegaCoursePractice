class Account():

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance = float(file.read())

    def withdraw(self, amount):
        self.balance -= amount
        
    def deposit(self, amount):
        self.balance += amount
        
    def commitToBank(self):
        with open(self.filepath, 'w') as file:
            file.write(str(8))


class Checking(Account):
    # These are doc-strings, and explain the purpose of your class (can be called on by {object instance.__doc__})
    """This class generates checking account objects"""
    type = "checking" # instance of class variable (shared by all instances of class, so static)
    def __init__(self, filepath, fee):
        super().__init__(filepath) # OR -> Account.__init__(self, filepath)
        self.fee = fee
    
    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# account = Account("App_Project_Practice/oop_practice/bankacc_ex/bank.txt")
john_account = Checking("john_bank.txt", 89)
josef_account = Checking("josef_bank.txt", 89)

print(f"Balance before any operations: {john_account.balance}")  # Initial balance check
john_account.transfer(111)
print(john_account.balance)
print(f"Balance after transfer: {josef_account.balance}")  # Balance after transfer
print(john_account.__doc__)

print()

print(f"Balance before any operations: {josef_account.balance}")  # Initial balance check
josef_account.transfer(10)
print(josef_account.balance)
print(f"Balance after transfer: {josef_account.balance}")  # Balance after transfer
print(josef_account.__doc__)