import math


class Student:
    # Encapsulation: Binding data and methods together
    # Also talks about, data access specifiers
    def __init__(self, name, age, maths, phy, che):
        self.name = name
        self.age = age
        self.maths = maths
        self.phy = phy
        self.che = che
        # End of function constructor

    def get_average(self):
        """
        Calculate and return the student average scores
        :return: Average of scores in maths, phy, che
        """
        self.avg = math.floor((self.maths + self.phy + self.che) / 3, )
        self.assign_grade()
        return self.avg
        # End of method get_average

    def assign_grade(self):
        if self.avg >= 75:
            self.grade = 'A'
        elif self.avg > 65:
            self.grade = 'B'
        else:
            self.grade = 'C'
        # End of method getGrade

    def print_student_details(self):
        print("---------Student Details for: ", self.name, "---------")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Maths: ", self.maths)
        print("Physics: ", self.phy)
        print("Chemistry: ", self.che)
        print("Average: ", self.get_average())
        print("Grade: ", self.grade)
        # End of method printStudentDetails

    def __del__(self):
        del self
        # End of Destructor method

    # End of class Student


stud1 = Student("Abhilash", 28, 55, 65, 88)
stud2 = Student("Sneha", 55, 67, 78, 87)
stud3 = Student("Mahesh", 33, 45, 65, 45)

stud1.print_student_details()
stud2.print_student_details()
stud3.print_student_details()
print("-----------------------------------------------")
