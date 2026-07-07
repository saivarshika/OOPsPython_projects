class ATM:

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Money Deposited Successfully")

        else:
            print("Invalid Amount")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid Amount")

        elif amount > self.__balance:
            print("Insufficient Balance")

        else:
            self.__balance -= amount
            print("Please Collect Cash")

    def check_balance(self):

        print("Current Balance:", self.__balance)


atm = ATM()

atm.deposit(5000)
atm.withdraw(1500)
atm.check_balance()