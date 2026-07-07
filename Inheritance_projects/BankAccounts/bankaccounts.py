class Account:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(Account):

    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest:", interest)


class CurrentAccount(Account):

    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Overdraft Limit Exceeded")


saving = SavingsAccount(1001, 10000, 5)
current = CurrentAccount(2001, 5000, 2000)

print("Savings Account")
saving.display()
saving.calculate_interest()

print()

print("Current Account")
current.display()
current.withdraw(6500)
print("Updated Balance:", current.balance)