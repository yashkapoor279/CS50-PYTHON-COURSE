def get_fullname(firstname,lastname):
  #returning full name in neated format
  full_name = f"{firstname} {lastname}"
  return full_name

# get_fullname("yash","kapoor") #this will not print anything because you need to store this print statement inside a variable to let return statement run

name=get_fullname("yash","kapoor")
print(name)
#return send a vlue back to the caller and func exits
#print displays info in the console nothing else 


#function naming must be meaningful
#length of function should be small
#avoid global variables - defined outside functions  - accessible throughtout the program