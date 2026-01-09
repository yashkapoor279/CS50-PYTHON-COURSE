def main():
  size = int(input("What is the size ?"))
  print_square(size)

#for each row in square
def print_square(size):
  #for each column
  for i in range(size):
    for x in range(size):
      print("#",end="")


      #prints a new line everytie you finish a new row 
    print()
    
  


main()