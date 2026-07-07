class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(self.name, "- ₹", self.price)


class Order:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_order(self):

        total = 0

        print("Order Details")
        print("-------------")

        for item in self.items:
            item.display()
            total += item.price

        print("-------------")
        print("Total Bill: ₹", total)


class Customer:

    def __init__(self, name, order):
        self.name = name
        self.order = order

    def show_customer(self):

        print("Customer:", self.name)
        self.order.show_order()


burger = MenuItem("Burger", 150)
pizza = MenuItem("Pizza", 300)
juice = MenuItem("Juice", 80)

order = Order()

order.add_item(burger)
order.add_item(pizza)
order.add_item(juice)

customer = Customer("Sai", order)

customer.show_customer()