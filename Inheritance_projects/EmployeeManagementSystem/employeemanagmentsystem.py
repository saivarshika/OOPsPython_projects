class Employee:

    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id

    def calculate_bonus(self):
        print("Bonus calculation is not defined.")


class Manager(Employee):

    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def calculate_bonus(self):
        bonus = self.team_size * 1000
        print("Manager Bonus:", bonus)


class Developer(Employee):

    def __init__(self, name, emp_id, tech_stack):
        super().__init__(name, emp_id)
        self.tech_stack = tech_stack

    def calculate_bonus(self):

        if self.tech_stack == "Python":
            bonus = 7000
        elif self.tech_stack == "Java":
            bonus = 6000
        else:
            bonus = 5000

        print("Developer Bonus:", bonus)


manager = Manager("Alice", 101, 8)
developer = Developer("Bob", 102, "Python")

print(manager.name)
print(manager.id)
print(manager.team_size)

manager.calculate_bonus()

print()

print(developer.name)
print(developer.id)
print(developer.tech_stack)

developer.calculate_bonus()