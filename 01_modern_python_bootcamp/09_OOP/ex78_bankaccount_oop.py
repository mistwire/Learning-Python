# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

user1 = BankAccount("Charlie")
user2 = BankAccount("Dr. Moneybags")

print(user1.owner, user1.balance)

user1.deposit(50)

print(user1.balance)

user1.withdraw(25)

print(user1.balance)

print(user2.owner, user2.balance)

user2.deposit(10000000.00)
user2.withdraw(1.5)

print(user2.owner, user2.balance)