# Write a program to input an integer N and print the sum of all its even digits
# and sum of all its odd digits separately.
# Digits mean numbers, not the places!
# That is, if the given integer is "13245",
# even digits are 2 & 4 and odd digits are 1, 3 & 5.

N = int(input())

even_sum = 0
odd_sum = 0

while(0 != N):
    r = N % 10
    if(r % 2 == 0):
        even_sum += r
    else:
        odd_sum += r
    N //= 10

print(even_sum, " ", odd_sum)