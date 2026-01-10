class Customer:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def intro(self):
    print("My name is",self.name,"I am",self.age,"years old")


c1=Customer("Yash",20)
c2=Customer("Palak",20)
c3=Customer("Adiedha",20)

L=[c1,c2,c3]  #collection of obj
for i in L:
  # print(i) #this will not print i , it will print address
  print(i.name,i.age,i.intro())