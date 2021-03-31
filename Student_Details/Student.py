class Student:
    def __init__(self, name, email, usn, college):
        self.Name = name
        self.Email = email
        self.USN = usn
        self.College = college

    def details(self):
        print(self.Name)
        print(self.Email)
        print(self.USN)
        print(self.College)

    def student_name(self):
        print(self.Name)

    def student_email(self):
        print(self.Email)

    def student_usn(self):
        print(self.USN)

    def student_college(self):
        print(self.College)


Name = input("Enter Student Name")
Email = input("Enter Student Email")
Usn = input("Enter USN")
College = input("Enter College Name")

obj = Student(Name, Email, Usn, College)
obj.details()
