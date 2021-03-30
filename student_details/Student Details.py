class StudentDetails:
    def __init__(self, n, e, u, c):
        self.name = n
        self.email = e
        self.college = c
        self.usn = u

    def getDetails(self):
        return self.name, self.email, self.college, self.usn