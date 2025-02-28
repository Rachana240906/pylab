class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display(self):
        print(f"Acc Number: {self.account_number}")
        print(f"Balance: {self.balance}")

account_number = input("Enter acc number: ")
balance = float(input("Enter balance: "))
account = BankAccount(account_number, balance)

while True:
    action = input("Enter action (deposit/withdraw/display/exit): ").lower()
    if action == "deposit":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif action == "withdraw":
        amount = float(input("Enter withdraw amount: "))
        account.withdraw(amount)
    elif action == "display":
        account.display()
    elif action == "exit":
        break
    else:
        print("Invalid")
