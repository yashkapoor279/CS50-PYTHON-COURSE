def main():
  print_column(3)

def print_column(height):
  for x in range(height):
    print("?", end="") #added a end to print it horizontally


main()