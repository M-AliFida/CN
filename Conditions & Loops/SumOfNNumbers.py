# Given an integer n, find and print the sum of numbers from 1 to n.

n = int(input())
i = 1
sum = 0

while(i <= n):
    sum += i
    i += 1

print(sum)