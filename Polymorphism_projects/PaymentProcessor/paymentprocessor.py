class Payment:

    def pay(self, amount):
        print("Processing payment...")


class CreditCard(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class Wallet(Payment):

    def pay(self, amount):
        print("Paid ₹", amount, "using Wallet")


payments = [
    CreditCard(),
    UPI(),
    Wallet()
]

amount = 1500

for payment in payments:
    payment.pay(amount)