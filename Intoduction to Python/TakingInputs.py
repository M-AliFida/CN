a = input()
b = input()
sum = a + b
print(sum) # The answer here for inputs 10 and 20 will be 1020 (concatenation). Input takes string.

sum = int(a) + int(b)
print(sum) # Here the answer is 30, after you have converted string to int.

c = int(input()) # Converts (type-casting) straight away
print(type(c)) # int

# Note. Can also use float conversion when taking input.
