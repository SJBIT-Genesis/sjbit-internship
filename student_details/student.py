class Student:
    def __init__(self, name, mobile, usn, email):
        self.name = name
        self.mobile = mobile
        self.usn = usn
        self.email = email


a = Student('purva', 9606239028, '1jb17cs120', 'purvarathod9@gmail.com')
print(a.name, a.mobile, a.usn, a.email)
