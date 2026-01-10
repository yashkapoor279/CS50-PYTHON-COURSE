#nested loop :  A loop inside another loop



rows = int(input("Enter rows"))
columns = int(input("Enter columns"))
symbol = input("Enter symbol")

#program to make rectangle of a single symbol
for i in range(rows): #prints it 2 times because (0,1) 2 is exclusive
  for x in range(columns):
   print(symbol , end=" ")
  print()  #make a new line #numbers displayed on the same line 



for i in range(0,2): #prints it 2 times because (0,1) 2 is exclusive
  for x in range(1,10):
   print(x , end="x ")
  print()  #make a new line #numbers displayed on the same line 



