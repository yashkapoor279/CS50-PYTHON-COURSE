#class-1
class Customer:
  def __init__(self,name,gender,address):
    self.name=name
    self.gender=gender
    self.address=address
 
  
#class-2
class Address:
  def __init__(self,city,pincode,state):
    self.city=city
    self.pincode=pincode
    self.state=state




add=Address("Sonipat","13123","Haryana")
cust=Customer("Binod","Male",add)



print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)