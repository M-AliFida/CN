# Doing operations on numbers -- standard BODMAS applies (just use brackets).

a = 10
b = 4

print(a + b)
print (a - b)
print (a * b)
print (a / b) # Will give floating value, unlike Java which does integer division.
print (a // b) # This is integer division (or, floor division), i.e. the answer is 2.
print (a ** 4) # Exponential, i.e. 10^4
print (a % b) # modulus

# Simple interest

p = int(input())
r = int(input())
t = int(input())

print((p * r * t) // 100)

# F to C conversion

f = int(input())
c = (f - 32) * 5 // 9

print(c)