# Given three numbers, which one is the largest

a = int(input())
b = int(input())
c = int(input())

if (a >= b) and (a >= c):
    print("a is the largest")
elif (b >= a) and (b >= c):
    print("b is the largest")
else:
    print("c is the largest")

# Conditionals with logical operators, multiple elifs.

n = int(input())

if (n > 10):
    print("red")
elif (n >= 5):
    print("green")
elif (n > 0):
    print("yellow")