#It's a good idea to close a file after usage as it will free up the resources
#If we dont close it, garbage collector would close it
#with keyword closes the file as soon as the usage is over

with open('sample1.txt','w') as f:
  f.write('Ram Ram ji')
  f.write('yes')
  