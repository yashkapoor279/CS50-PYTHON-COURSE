#moving within a file
with open('sample.txt','r') as f:
  print(f.read(10)) #prints first 10 char
  print(f.read(10))
  print(f.read(10))
  print(f.read(10))