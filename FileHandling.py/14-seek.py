with open('sample.txt','r') as f:
  print(f.read(10))
  print(f.seek(2))#moves buffer to specified position
  print(f.read(10))
  print(f.tell())#where the current buffer currently

