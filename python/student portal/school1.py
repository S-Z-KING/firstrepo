class school:
    pass

class Student(school):
    def __init__(
        self,
        student_id,
        student_name,
        student_f_name,
        student_phone_number,
        student_address,
        student_fees
        ):
        self.student_id = student_id
        self.student_name = student_name
        self.student_f_name = student_f_name
        self.student_phone_number = student_phone_number
        self.student_address = student_address
        self.student_fees = student_fees

    def getStudent(self):
        return f"id = {self.student_id} ,name = {self.student_name} ,father name = {self.student_f_name} ,phone number = {self.student_phone_number} ,address = {self.student_address} ,fee = {self.student_fees}"

class Teacher(school):
    def __init__(
        self,
        teacher_id,
        teacher_name,
        teacher_f_name,
        teacher_phone_number,
        teacher_address       
        ):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_number
        self.teacher_address = teacher_address   
  
    def getTeacher(self):
        return f"id = {self.teacher_id} ,name = {self.teacher_name} ,father name = {self.teacher_f_name} ,phone number = {self.teacher_phone_number} ,address = {self.teacher_address}"

class Classrooms(school):
    def __init__(self, class_name, class_time):
        self.class_name = class_name
        self.class_time = class_time

    def getClassrooms(self):
        return f"name = {self.class_name}, time = {self.class_time}"

class admin(school):
    pass


student1 = Student(
    "1",
    "Ali",
    "Usman",
    "92389297012",
    "Manzoor colony Karachi",
    "1000"
)

v = student1.getStudent()

print(v)