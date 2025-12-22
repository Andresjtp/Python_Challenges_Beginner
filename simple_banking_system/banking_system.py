import random


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.account_number = random.randint(100000, 999999)


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account):
        self.accounts.append(account)

    def deposit(self, account_name, amount):
        for account in self.accounts:
            if account_name.lower() == account.owner.lower():
                account.balance += amount
            print(f"Deposited ${amount}. New balance: ${account.balance}")
            return
        print("No account with this name found")

    def withdraw(self, account_name, amount):
        for account in self.accounts:
            if account_name.lower() == account.owner.lower():
                if amount > account.balance:
                    print("Insufficent funds available")
                    return
                account.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${account.balance}")
                return
            print("No accounts with this name found")

    def account_info(self):
        for account in self.accounts:
            print(
                f"Account name: {account.owner}\nAccount Balance: {account.balance}\nAccount Number: {account.account_number}"
            )
