#yield statement #generator - generate a single value at one tiime
def countdown(num):
  while num >0:
    yield num
    num-=1

#using generator 
for number in countdown(9):
  print(number)
