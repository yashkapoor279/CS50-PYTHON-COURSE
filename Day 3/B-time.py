#displays Time's Up after a fixed interval of time 
import time 


my_time=int(input("Enter the time in seconds"))

for x in range(0,my_time):
# for x in range(my_time,0,-1): #5 4 3 2 1
  
  print(x)
  time.sleep(1)  #it will stop for 1 sec after each iteration and then print the next iteration



print("Time's UP")