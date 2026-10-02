class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("You cannot deposit negative amounts")
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("You cannot withdraw negative amounts")
            return
        if amount > self.balance:
            print("Amount is more than the balance, you cannot withdraw.")
        else:
            self.balance -= amount

    def show_info(self):
        print(f"Account owner: {self.owner}, balance: {self.balance}")

acc = BankAccount("Bilol", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(1000)
acc.show_info()