n = int(input())
i = 2
flag = True

while(i < n):
    if(n % i == 0):
        flag = False
        break
    else:
        i += 1

if(flag):
    print("Prime")
else:
    print("Not Prime")