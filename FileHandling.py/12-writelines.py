L=["Honesty is the Best Policy\n" for i in range (100)]

with open('sample2.txt','w') as f:
  f.writelines(L)