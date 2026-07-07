class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year):

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True

        return False

    @classmethod
    def from_string(cls, date_string):

        year, month, day = date_string.split("-")

        return cls(int(day), int(month), int(year))

    def display(self):
        print(f"{self.day:02d}-{self.month:02d}-{self.year}")


date1 = Date.from_string("2026-04-05")

print("Date:")
date1.display()

print()

print("Leap Year Check")
print(Date.is_leap_year(2024))
print(Date.is_leap_year(2023))