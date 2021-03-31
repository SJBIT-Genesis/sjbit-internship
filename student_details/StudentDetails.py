class StudentDetails:
    def __init__(self, name, email, usn, college):
        self.name = name
        self.email = email
        self.usn = usn
        self.college = college

    def student_details(self):
        print(self.name)
        print(self.email)
        print(self.usn)
        print(self.college)


obj = StudentDetails("gowrika", "gowrikachoudhary@gmail.com", "1jb17cs050", "SJB")
obj.student_details()
