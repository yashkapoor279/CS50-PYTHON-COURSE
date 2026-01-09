l1=[1,2,3,4]
l2 = l1 #aliasing one list to another
#two variables pointing to one list 

print(l2)
#but if we try to change the dta in one list it will be changed in both of the list for example 

l2[1]=52

print(l1,l2)

#the solution for this is the copy method