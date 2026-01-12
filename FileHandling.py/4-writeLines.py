#writeLines help us to write multiple lines at once

L=["My name is Yash\n","I am 20 years old\n","I am pursuing CSE"]

f=open('sample.txt','w')
f.writelines(L)
f.close()