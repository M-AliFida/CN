# n = int(input())
# m = int(input())
#
# if (n % 2 == 0):
#     if(m % 2 == 0):
#         print("1")
#     else:
#         print("2")
# else:
#     print("3")

a = True
b = True
c = False
d = False

if a or b: # True
    if c and b or d: # False or # False
        print('A')
    elif c and c or a and a: # True -- so it will print here.
        print('B')
    else:
        print('C')
else:
    print('D')