class StudentDetails:
    def __init__(self,name,email,usn,phone):
        self.name = name
        self.email = email
        self.usn = usn
        self.phone = phone

    def display(self):
        print(self.name,self.email,self.usn,self.phone)


S=StudentDetails("AKASH","abc@gmail.com","1jb17cs008","9031190322")
S.display();