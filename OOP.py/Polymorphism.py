# Polymorphism in object-oriented programming is the ability of different objects to respond to the same method call in their own way, typically achieved through method overriding (runtime polymorphism) and method overloading (compile-time polymorphism)

#Method overriding
class Phone:
  def __init__(self,name ,brand, price):
    self.name = name
    self.price=price
    self.brand=brand

  def buy(self):
    print("Buying a phone")

class Sphone(Phone):
  
  
  def buy(self):
    print("Buying a Smartphone")#this will be printed because of method overriding -.polymorphism ....Sphone jb call hua to bhale hi parent class call hoga pr iska function uske function ko override krdeg

s=Sphone("Realme","9i","11000")
s.buy()
