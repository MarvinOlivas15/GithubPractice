#Class is a blueprint of an object
class Student:
    #constructor initializer
    #attributes
    def __init__(self, first_name, last_name, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grade
        self.email = first_name + last_name + '@weber.edu'

    def print_student_data(self):
        print (f"Student info \n" ,
            f"\tFirst Name: {self.first_name} \n" ,
            f"\tLast Name: {self.last_name} \n",
            f"\tGrade: {self.grade}\n" ,
            f"\tEmail: {self.email}")
    
    def change_grade(self, new_grade_level):
        self.grade = new_grade_level 

#marvin_olivas is an instance of the student class
marvin_olivas = Student("Marvin", "Olivas", "Sophomore") #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior") #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")

marvin_olivas.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()

marvin_olivas.change_grade("Junior")
jane_doe.change_grade("Graduated")
waldo_wildcat.change_grade("Freshman")

marvin_olivas.print_student_data()
jane_doe.print_student_data()
waldo_wildcat.print_student_data()

# We Created the OOP branch 