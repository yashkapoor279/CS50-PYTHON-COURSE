class Phone:
  def __init__(self,name ,brand, price):
    self.name = name
    self.price=price
    self.brand=brand

  def buy(self):
    print("Buying a phone")

class Sphone(Phone):
  
  
  def buy(self):
    print("Buying a Smartphone")
    super().buy() #super keyword help to call the memeber function in the parent class...this is used to avoid method overriding



s=Sphone("Realme","9i","11000")
s.buy()


#output :)
#Buying a Smartphone -> first child class
#Buying a phone -> then parent class
