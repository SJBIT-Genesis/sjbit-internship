class Student:
    def __init__(self, name, mobile, usn, email):
        self.name = name
        self.phone = mobile
        self.usn = usn
        self.email = email

a = Student('Sonika', 7619235265, '1JB17CS155', 'sonikaprathiraj06@gmail.com')
print(a.name, a.phno, a.usn,a.email)