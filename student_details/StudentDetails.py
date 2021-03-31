class StudentDetails:
    def __init__(self, name, email, usn, college):
        self.name = name
        self.email = email
        self.usn = usn
        self.college = college
    def my_func(self):
        print(self.name, self.email, self.usn, self.college)