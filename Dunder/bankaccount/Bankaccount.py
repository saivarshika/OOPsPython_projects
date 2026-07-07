class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):

        total = self.balance + other.balance

        return BankAccount(
            self.name + " & " + other.name,
            total
        )

    def __gt__(self, other):
        return self.balance > other.balance

    def __str__(self):
        return f"{self.name} : ₹{self.balance}"


acc1 = BankAccount("Sai", 5000)
acc2 = BankAccount("Rahul", 7000)

merged = acc1 + acc2

print("Merged Account")
print(merged)

print()

if acc1 > acc2:
    print(acc1.name, "has more balance")
else:
    print(acc2.name, "has more balance")