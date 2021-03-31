class Studentdetails:
    def __init__(self,name,email,usn,college):
        self.name=name
        self.email=email
        self.usn=usn
        self.college=college

    def display(self):
        print(self.name,self.email,self.usn,self.college)

Student = Studentdetails("keerthi","mkeerthi@gmail.com","62","sjbit")
Student.display()

