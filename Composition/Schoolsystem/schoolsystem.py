class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Student:", self.name)


class Teacher:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Teacher:", self.name)


class Classroom:

    def __init__(self, room_name, teacher):
        self.room_name = room_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display(self):

        print("Classroom:", self.room_name)

        self.teacher.display()

        print("Students:")

        for student in self.students:
            student.display()


class School:

    def __init__(self, name):
        self.name = name
        self.classrooms = []

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def display(self):

        print("School:", self.name)

        for classroom in self.classrooms:
            print()
            classroom.display()


teacher1 = Teacher("Mr. Sharma")

student1 = Student("Rahul")
student2 = Student("Anjali")
student3 = Student("Sai")

classroom1 = Classroom("Class 10-A", teacher1)

classroom1.add_student(student1)
classroom1.add_student(student2)
classroom1.add_student(student3)

school = School("ABC Public School")

school.add_classroom(classroom1)

school.display()