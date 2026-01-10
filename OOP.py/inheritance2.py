class Phone:
  def __init__(self,name ,brand, price):
    self.name = name
    self.price=price
    self.brand=brand

class Sphone(Phone):
  pass

s=Sphone("Xiomi","12f",30000)
print(s.price)
print(s.brand)
# print(s.__brand) #child class cannot inherit pvt members of a parent class