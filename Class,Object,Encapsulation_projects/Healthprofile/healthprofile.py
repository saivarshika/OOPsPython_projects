class HealthProfile:

    def __init__(self, weight, height):
        self.__weight = weight
        self.__height = height

    def calculate_bmi(self):

        bmi = self.__weight / (self.__height ** 2)

        print("Your BMI is:", round(bmi, 2))

    def update_weight(self, new_weight):

        if new_weight > 0:
            self.__weight = new_weight
            print("Weight updated successfully.")

        else:
            print("Invalid weight.")


person = HealthProfile(70, 1.75)

person.calculate_bmi()

person.update_weight(75)

person.calculate_bmi()