class Student:
    def __init__(self, name, phno, usn, email):
        self.name = name
        self.phno = phno
        self.usn = usn
        self.email = email

    def print_details(self):
        print(self.name, self.phno, self.usn, self.email)