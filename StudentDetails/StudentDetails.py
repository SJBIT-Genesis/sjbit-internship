class StudentDetails:
    def __init__(self, n, e, c, p):
        self.name = n
        self.email = e
        self.college = c
        self.phno = p

    def print_details(self):
        print('Name:', self.name)
        print('Email:', self.email)
        print('College:', self.college)
        print('Ph No:', self.phno)