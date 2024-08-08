class Course:
    
    def __init__(self,course_name,instructor,):
        """function for initializing all class attributes"""
        self.course_name = course_name
        self.instructor = instructor
        self.students = []

    def add_student(self,name,age,grade):
        """function for adding a student"""
        student = {"name": name, "age":age, "grade":grade }
        self.students.append(student)

    def remove_student(self,name):
        """function for remove a student"""
        self.students = [student for student in self.students if student['name'] != name]

    def update_student(self,name,new_name=None,new_age=None,new_grade=None):
        """function for update student data"""
        for student in self.students:
            if student['name'] == name:
                if new_name is not None:
                    student['name'] = new_name
                elif new_age is not None:
                    student['age'] = new_age
                elif new_grade is not None:
                    student['grade'] = new_grade
                break

    def __repr__(self):
        """function to print out the course class and it content"""
        return (f"Course(course_name='{self.course_name}', instructor='{self.instructor}', "
                f"students={self.students})")


course = Course("backend", "Nat")
course.add_student("sadiq", 19, 90)
course.add_student("iysha", 22, 85)
course.update_student('sadiq',new_age=21)
course.remove_student('Alice')


print(course)

                    
