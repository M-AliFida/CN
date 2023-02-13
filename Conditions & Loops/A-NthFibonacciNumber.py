# Nth term of Fibonacci series F(n), where F(n) is a function,
# is calculated using the following formula -
#     F(n) = F(n-1) + F(n-2),
#     Where, F(1) =  1,
#            F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number.

N = int(input())
f1 = 1
f2 = 1

if (N == 1 or N == 2):
    print(int(1))
else:
    i = 1
    while(i <= N - 2):
        f3 = f2 + f1
        f1 = f2
        f2 = f3
        i += 1

    print(f2)