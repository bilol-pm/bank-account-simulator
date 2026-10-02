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

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * self.interest_rate / 100
        self.balance += interest_amount

acc = BankAccount("Bilol", 100)
interest = SavingsAccount("Bob", 100, 5)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(1000)
acc.show_info()
interest.add_interest()
interest.show_info()