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


def create_account():
    print("\n=====CREATE ACCOUNT=====")
    print("Please, first create account!")
    owner_name = input("Enter your name: ")

    while True:
        owner_balance = input("Enter your starting balance: ")
        if not owner_balance.isdigit():
            print("You must enter a number")
            continue
        break
    owner_balance = int(owner_balance)
    return BankAccount(owner_name, owner_balance)

def show_main_menu():
    print("\n=====BANK MENU=====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Showing Information")
    print("4. Exit")


def main():
    account = create_account()

    while True:
        show_main_menu()
        choice = input("> ").strip()
        if choice == "1":
            amount_balance = input("Enter your amount balance: ")
            amount_balance = int(amount_balance)
            account.deposit(amount_balance)
        elif choice == "2":
            amount_withdraw = input("Enter your amount withdraw: ")
            amount_withdraw = int(amount_withdraw)
            account.withdraw(amount_withdraw)
        elif choice == "3":
            account.show_info()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




