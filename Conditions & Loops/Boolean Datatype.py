# Conditions:  True and False

a = True
b = False

# Relational Operators

a = 10
b = 20

print(a > b)
print(a < b)
print(a >+ b)
print(a <= b)
print(a == b) # Obviously not to be confused with assignment '='
print(a != b)

# Logical Operators, which operates on booleans.

c1 = a >= 10
c2 = b > 10

print("---------")
print(c1 and c2) # and is true and true
print (c1 or c2) # or is true and false / false and true
print(not(c1)) # negation (just flips it)