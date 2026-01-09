"""
[expression for item in iterable if condition]

exp : e*2 
item - 
terable - range(1,11)
condition optional
"""

# squares = [] traditional ways
# for i in range(1,11):
#   squares.append(i**2)

# print(squares)

squares = [i**2 for i in range(1,11) if i%2==0]
print(squares) 