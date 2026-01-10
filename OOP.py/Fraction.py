#what if i want to show the fraction as 4/5 -- we will use magic method 
#constructors are also called magic methods 
#__str__
#__add__

#building our own datatype
class Fraction:
  def __init__(self,n,d):
    self.num=n
    self.den=d
  

  def __str__(self): #sub,add , mul are constructors to perform various respective opertions
    return 'Hello'
  #addition constructor
  def __add__(self,other):
    temp_num=self.num*other.den+self.den*other.num
    temp_den=self.den*other.den
 
    return "{}/{}".format(temp_num,temp_den)
  
  #subtraction constructor
  def __sub__(self,other):
    temp_num=self.num*other.den-self.den*other.num
    temp_den=self.den*other.den

    return "{}/{}".format(temp_num,temp_den)
  
  #multiplication constructor
  def __mul__(self,other):
    temp_num=self.num*other.num
    temp_den=self.den*other.den

    return "{}/{}".format(temp_num,temp_den)
  

  #division constructor
  def __truediv__(self,other):  #other k fraction ko ulta krke add
    temp_num=self.num*other.den
    temp_den=self.den*other.num

    return "{}/{}".format(temp_num,temp_den)

x=Fraction(4,5)
# print(type(x))  #this will print fraction -- we have created our own datatype
print(x)

y = Fraction(6,8)
print(y)

print(x+y)
print(x-y)
print(x*y)
print(x/y)


#what if i want to show the fraction as 4/5 -- we will use magic method 
#constructors are also called magic methods 
#__str__
#__add__
