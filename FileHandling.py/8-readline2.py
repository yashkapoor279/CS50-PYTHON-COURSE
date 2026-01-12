#read entire text by using readline 

f=open('sample.txt','r')

while True:
  data =f.readline()
  if data =='':
    break
  else:
    print(data,end='')

f.close()
