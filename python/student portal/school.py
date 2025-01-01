class School:
    pass

class Student(School):
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
        return f"id = {self.student_id},name = {self.student_name},father name = {self.student_f_name},phone number = {self.student_phone_number},address = {self.student_address},fee = {self.student_fees}"

class Teacher(School):
    def __init__(
        self,
        teacher_id,
        teacher_name,
        teacher_f_name,
        teacher_phone_number,
        teacher_address,
        ):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_number
        self.teacher_address = teacher_address      

    def getTeacher(self):    
        return f"id = {self.teacher_id},name = {self.teacher_name},father name = {self.teacher_f_name},phone number = {self.teacher_phone_number},address = {self.teacher_address}" 

class Classrooms(School):
    def __init__(self, class_number, class_name, class_time):
        self.class_number = class_number
        self.class_name = class_name
        self.class_time = class_time

    def getClassrooms(self):
        return f"name = {self.class_name},time = {self.class_time}"

class Admin(School):
    pass

student1 = Student(
    "1",
    "Ali",
    "Usman",
    "923163425678",
    "Azam Town Karachi",
    "1000"
)
student2 = Student(
    "2",
    "Abdullah",
    "Ikraam",
    "923224536738",
    "Manzoor Colony Karachi",
    "1500"
)
student3 = Student(
    "3",
    "Shoaib",
    "Shakeel",
    "923453678989",
    "Azam Town Karachi",
    "1500"
)
student4 = Student(
    "4",
    "Abdullah",
    "Ikraam",
    "923224536738",
    "Manzoor Colony Karachi",
    "1500"
)
student5 = Student(
    "5",
    "Talha",
    "IQbal",
    "923343647896",
    "Azam Town Karachi",
    "2000"
)
student6 = Student(
    "6",
    "Abdullah",
    "Raees khan",
    "923476789684",
    "Manzoor Colony Karachi",
    "2500"
)
# information = student1.getStudent()
# print(information)
# information = student2.getStudent()
# print(information)
# information = student3.getStudent()
# print(information)
# information = student4.getStudent()
# print(information)
# information = student5.getStudent()
# print(information)
# information = student6.getStudent()
# print(information)

teacher1 = Teacher(
    "1",
    "Aqib",
    "Ali",
    "923645859098",
    "Admin Society Mehmoodabad Karachi",
)
teacher2 = Teacher(
    "2",
    "Asif",
    "Amir",
    "923453637856",
    "Admin Society Mehmoodabad Karachi",
)
teacher3 = Teacher(
    "3",
    "Samad",
    "Waqar",
    "923567598448",
    "Admin Society Mehmoodabad Karachi",
)
teacher4 = Teacher(
    "4",
    "Zain",
    "Zahoor",
    "923796768543",
    "Admin Society Mehmoodabad Karachi",
)
teacher5 = Teacher(
    "5",
    "Zahid",
    "Shahid",
    "923354768464",
    "Admin Society Mehmoodabad Karachi",
)
teacher6 = Teacher(
    "6",
    "Mehmood",
    "Wassey",
    "923674836467",
    "Admin Society Mehmoodabad Karachi",
)

# information = teacher1.getTeacher()
# print(information)
# information = teacher2.getTeacher()
# print(information)
# information = teacher3.getTeacher()
# print(information)
# information = teacher4.getTeacher()
# print(information)
# information = teacher5.getTeacher()
# print(information)
# information = teacher6.getTeacher()
# print(information)

classroom1 = Classrooms(
    "1",
    "AI",
    "2:00 to 3:30"
)
classroom2 = Classrooms(
    "2",
    "WEB",
    "3:30 to 5:00"
)
classroom3 = Classrooms(
    "3",
    "MS",
    "9:00 to 12:00"
)
classroom4 = Classrooms(
    "4",
    "English Language",
    "2:00 to 3:30"
)
classroom5 = Classrooms(
    "5",
    "Digital Marketting",
    "11:00 to 1:00",
)
classroom6 = Classrooms(
    "6",
    ""
)

AIclass = classroom1.getClassrooms()
print(AIclass)
