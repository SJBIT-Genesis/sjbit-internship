class Student:
    def __init__(self,name,phno,usn,email):
        self.name = name
        self.phno = phno
        self.usn = usn
        self.email = email


a=Student('sachu',7847896697,'1JB17CS128','sachulokesh@gmail.com')
print(a.name,a.phno,a.usn,a.email)