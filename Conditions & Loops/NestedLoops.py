# Print all prime numbers from 2 to n.

n = int(input())
i = 2

# Outer loop. E.g. i = 5
while (i <= n):
    flag = True # Both of these variables with reset with each iteration.
    j = 2

    # Inner loop. E.g. 2 to 4 to check if 5 is a prime. The problem this loops solves is if j is a prime number.
    while(j < i):
        if(i % j == 0):
            flag = False
            break
        else:
            j += 1

    if(flag):
        print(i)

    i += 1