class Student:
    def __init__(self, name, phno, usn, email):
        self.name = name
        self.phno = phno
        self.usn = usn
        self.email = email


a = Student('Suraj', 9591526424, '1JB17CS159', '20.surajraju@gmail.com')
print(a.name, a.phno, a.usn, a.email)