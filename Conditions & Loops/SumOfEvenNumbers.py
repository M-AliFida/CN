# Given a number N, print sum of all even numbers from 1 to N.

n = int(input())
i = 1
sum = 0

while(i <= n):
    if (i % 2 == 0):
        sum += i
    i += 1

print(sum)

# # Alternate
#
# n = int(input())
# i = 2
# sum = 0
#
# while(i <= n):
#   sum += i
#   i += 2
#
# print(sum)

