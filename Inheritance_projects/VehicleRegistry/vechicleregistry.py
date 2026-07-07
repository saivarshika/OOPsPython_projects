class Vehicle:

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def fuel_efficiency(self):
        print("Fuel efficiency is not defined.")


class Car(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Car Fuel Efficiency: 18 km/l")


class Bike(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Bike Fuel Efficiency: 45 km/l")


class Truck(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Truck Fuel Efficiency: 8 km/l")


car = Car("Petrol")
bike = Bike("Petrol")
truck = Truck("Diesel")

print("Car Fuel Type:", car.fuel_type)
car.fuel_efficiency()

print()

print("Bike Fuel Type:", bike.fuel_type)
bike.fuel_efficiency()

print()

print("Truck Fuel Type:", truck.fuel_type)
truck.fuel_efficiency()
class Vehicle:

    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def fuel_efficiency(self):
        print("Fuel efficiency is not defined.")


class Car(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Car Fuel Efficiency: 18 km/l")


class Bike(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Bike Fuel Efficiency: 45 km/l")


class Truck(Vehicle):

    def __init__(self, fuel_type):
        super().__init__(fuel_type)

    def fuel_efficiency(self):
        print("Truck Fuel Efficiency: 8 km/l")


car = Car("Petrol")
bike = Bike("Petrol")
truck = Truck("Diesel")

print("Car Fuel Type:", car.fuel_type)
car.fuel_efficiency()

print()

print("Bike Fuel Type:", bike.fuel_type)
bike.fuel_efficiency()

print()

print("Truck Fuel Type:", truck.fuel_type)
truck.fuel_efficiency()