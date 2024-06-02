
class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def get_age(self):
        print(f"Age:{self.age}")

    def get_name(self):
        print(f"Name:{self.name}")


class Employee(Person):
    def __init__(self, name, age, id, salary):
        super().__init__(name, age)
        self.id = id
        self.salary = salary

    def display(self):
        print(f"id:{self.id} \nsalary:{self.salary}")

class Inheritance:
    def main():
        person_object = Employee("abc", 30, 45, 50000)
        person_object.get_name()
        person_object.get_age()
        person_object.display()

Inheritance.main()


# Performing Crud operations in Student data without using SELF
class Student:
    student_list = list()

    def add():

        records_count = int(
            input("please enter how many records you want to add:"))
        for count in range(records_count):

            student_data = {"Name": input("Enter Name:-"),
                            "Gender": input("Enter gender:-"),
                            "roll": int(input("Enter roll:-"))}

            Student.student_list.append(student_data)

    def show():
        key = input("Enter student name in the record:-")
        flag = False
        for record in Student.student_list:
            if record["Name"] == key:
                flag = True
                print("Name=", record["Name"])
                print("Gender=", record["Gender"])
                print("roll=", record["roll"])
                break

        if not flag:
            print("Student name not in the records")

    def remove():
        key = input("Enter student name for removing in records:-")
        flag = False
        for record in Student.student_list:
            if record["Name"] == key:
                flag = True
                Student.student_list.remove(record)
                break

        if not flag:
            print("Student record Found")

if __name__ == '__main__':
    Student.add()
    Student.show()
    Student.remove()
    Student.show()

print("to show the student details:")
for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

print("\nnew details adding into student class:")
Student.student_hobby = 'VII'


for key, value in Student.__dict__.items():
    if not key.startswith('_'):
        print(f'{key} -> {value}')

    for record in range(students_list.__len__()):
        s.display(students_list[record])
else:
    print("Invalid choice")

#  Performing Student Crud operations using dictionary
class student:
    student_dict = {}
    key = 0

    def add_student(self):

        self.n = int(input('how many entries'))
        for record in range(0, self.n):
            self.l1 = []
            self.student_name = input('enter student name ')
            self.student_rollno = int(input('enter student rollno '))
            self.student_class = input('enter studnet class')

            self.l1.append(self.student_name)
            self.l1.append(self.student_rollno)
            self.l1.append(self.student_class)

            self.key = self.key+1
            self.student_dict[self.key] = self.l1

    def show_student(self):
        self.record = int(input('enter key to display'))
        print(self.student_dict)
        self.values1 = self.student_dict[self.record]
        print(self.values1)

    def remove_student(self):
        self.removekey = int(input('enter key to remove'))
        if self.removekey in self.student_dict:
            del self.student_dict[self.removekey]

def remove_student(self):
    self.removekey = int(input('enter key to remove'))
    if self.removekey in self.student_dict:
        del self.student_dict[self.removekey]
        print(f'{self.removekey} is removed')
    else:
        print('invalid key')
    print(self.student_dict)


def main():
    s1 = student()
    s1.add_student()
    s1.show_student()
    s1.remove_student()

main()                                                                                                                                     output: -how many entries2

class Student:
    name = ' '
    clg = ' '
    rno = 0

    def add(self, name, clg, rno):
        self.name = name
        self.clg = clg
        self.rno = rno

