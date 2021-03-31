class StudentDetails:
    def __init__(self,name,email,usn,college):
        self.name=name
        self.email=email
        self.usn=usn
        self.college=college

    def display(self):
        print(self.name,self.email,self.usn,self.college)

Student = StudentDetails("Nisha","nishagowda1310@gmail.com","1jb17cs090","SJBIT")
Student.display()