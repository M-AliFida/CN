# Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
# Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.

N = int(input())
reverse = 0

while(N > 0):
    r = N % 10
    N = N // 10 # Reminder to use INTEGER DIVISION
    reverse = (reverse * 10) + r

print(reverse)

# OG Solution:


# N = int(input())
# reverse = 0
#
# while(N > 0):
#     reverse *= 10
#     r = int(N % 10)
#     reverse += r
#     N = int(N / 10)
#
# print(reverse)