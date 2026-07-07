class User:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        return cls(name, "Admin")

    @classmethod
    def create_guest(cls, name):
        return cls(name, "Guest")

    def display(self):
        print("Name :", self.name)
        print("Role :", self.role)


admin = User.create_admin("Sai")
guest = User.create_guest("Rahul")

print("Admin Details")
admin.display()

print()

print("Guest Details")
guest.display()