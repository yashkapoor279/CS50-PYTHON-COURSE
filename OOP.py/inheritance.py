class User:  #parent class
  def login(self):
    print("Login")
  def register(self):
    print("Register")
class student(User): #child class inherited from user class
  def enroll(self):
    print("enroll")
  def review(self):
    print("review")

#object declaration

st1=student()

st1.enroll()
st1.review()
st1.login()
st1.register()

#student(child class) can inherit properties from user class but user cannot inherit properties from student...inheritance moves down to up

# u=User()

# u.enroll()
# u.review()
# u.login()
# u.register() #prints an error


