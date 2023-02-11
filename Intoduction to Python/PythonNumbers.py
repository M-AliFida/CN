a1 = 23
a2 = 3.4
a3 = 4 + 5j

print(a1) # int
print(a2) # float
print(a3) # complex

a = 10
print(id(a))
a = a + 1 # Evaluation done first, then address is redirected
print(id(a)) # id has changed

print("----------")

a = 10
b = 10
print(id(a))
print(id(b)) # optimisation -- ID is the same (-5 to 256), as the value is the same

# In Python, the values are stored in a separate memory.
# The variable stores address/ id of the value.
# Hence, if the value is the same, the variables will point to the same address (within limits).