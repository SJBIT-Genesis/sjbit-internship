class StudentDetails:
    def __init__(self,name,email,usn,college):
        self.name=name
        self.email=email
        self.usn=usn
        self.college=college

    def display(self):
        print(self.name,self.usn,self.email,self.college)

Student=StudentDetails("nidhi","nidhi@gmail.com","78","sjbit")
Student.display()
