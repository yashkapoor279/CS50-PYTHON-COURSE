class Customer:
  def __init__(self,name,gender):
    self.name = name
    self.gender=gender
  

def greet(Customer):
  pass
  
cust = Customer("Palak")
print(id(cust))

greet(cust)