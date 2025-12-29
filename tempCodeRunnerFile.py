#ask user for their name 
name = input("What's your name?")

name = name.strip() #removing white spaces from the starting 

#name = name.capitalize() #Capitalize the very first letter of the user's name

name = name.title() #Capitalize each letter of a word

#name = name.strip().title() #strip of the white space and capitalize first letter of each word 


#Split username to user's first and last name 
first , last = name.split(" ")
print(f"hello , {first}") 
print(f"hello , {last}") 

#say hello to user
print("hello",name) # yash's hello to the world
print("hello",name , sep="--") #printing hello yash with a separator


#print("hello , \"friend\"")  #printing double quotes in the output 
print(f"hello , {name}") #classified as a special string
