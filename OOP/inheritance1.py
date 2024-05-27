class Users:

    def login(self):
        print("Login")
    def register(self):
        print("Register")

class Student(Users):

    def enroll(self):
        print("Enroll")
    def review(self):
        print("Review")

s = Student()
s.enroll()
s.review()
s.login()