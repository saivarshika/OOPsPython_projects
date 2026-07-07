class CPU:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("CPU:", self.brand)


class RAM:

    def __init__(self, size):
        self.size = size

    def show(self):
        print("RAM:", self.size, "GB")


class Storage:

    def __init__(self, storage_type, capacity):
        self.storage_type = storage_type
        self.capacity = capacity

    def show(self):
        print("Storage:", self.capacity, "GB", self.storage_type)


class Computer:

    def __init__(self, cpu, ram, storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def assemble(self):

        print("Computer Configuration")
        print("----------------------")

        self.cpu.show()
        self.ram.show()
        self.storage.show()


cpu = CPU("Intel i7")
ram = RAM(16)
storage = Storage("SSD", 512)

computer = Computer(cpu, ram, storage)

computer.assemble()