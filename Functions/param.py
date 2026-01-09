"""
parameters - placeholder for the values
arguments - values
"""
#postional arg
def greet(name , city ): #parameter - name
  """displaying a hello message to user"""
  print(f"hello , {name} welcome to {city}" )

greet("palku" , "sonipat") #argument

#keyword
def greet(name , city ): #parameter - name
  """displaying a hello message to user"""
  print(f"hello , {name} welcome to {city}" )

greet(city = "sonipat",name="palku" ) #values key k aage hi paas krdi phir chahe baad mei ho ya pehele

#default
def greet(name = "Yash" , city ="Mumbai" ):#agr koi value pass nhi hogi to y values default aajayegi
  """displaying a hello message to user"""
  print(f"hello , {name} welcome to {city}" )

greet()

#positional arg
#keyword arg
#default arg