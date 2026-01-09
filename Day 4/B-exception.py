#syntax error : the error caused by the user and need to be fixed by the user himself 
#try block - risky code is written in it 
try:
   x = int(input("what's x? "))
   print(f"x is {x}")
except ValueError:  #if a error is found this particular block is run
   print("x is not an integer")
