#finding common element from two sets
l1=[34,-65,87,23,76,45]
l2=[34,65,23,85,69,87]

#set function
s1 = set(l1)
s2=set(l2)

s3=s1.intersection(s2)

print(list(s3))