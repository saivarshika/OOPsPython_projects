class BankAccount:

    interest_rate = 5

    def __init__(self, holder, account_number, balance):

        self.holder = holder
        self.account_number = account_number
        self.balance = balance

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def is_valid_account(number):

        return len(number) == 10 and number.isdigit()

    def display(self):

        print("Holder :", self.holder)
        print("Account Number :", self.account_number)
        print("Balance : ₹", self.balance)
        print("Interest Rate :", BankAccount.interest_rate, "%")


acc1 = BankAccount("Sai", "1234567890", 5000)
acc2 = BankAccount("Rahul", "9876543210", 8000)

print("Before Updating Interest Rate")
acc1.display()
print()
acc2.display()

BankAccount.set_interest_rate(7)

print("\nAfter Updating Interest Rate")
acc1.display()
print()
acc2.display()

print("\nAccount Validation")
print(BankAccount.is_valid_account("1234567890"))
print(BankAccount.is_valid_account("12AB567890"))