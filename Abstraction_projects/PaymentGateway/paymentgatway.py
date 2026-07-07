from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class Wallet(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet")


payments = [
    CreditCard(),
    UPI(),
    Wallet()
]

for payment in payments:
    payment.pay(2000)