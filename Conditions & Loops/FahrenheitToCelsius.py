# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W),
# you need to convert all Fahrenheit values from Start to End at the gap of W,
# into their corresponding Celsius values and print the table.

S = int(input())
E = int(input())
W = int(input())

while(S <= E):
    C = (int) ((S - 32) * 5/9)
    print (str(S) + " " + str(C))
    S += W


# Important note, rounding down works differently for negative numbers vs. truncating. Rounding down moves away from 0.
# Basically, rounding will always result in going lower or equal to the original number.
# Truncating moves closer to zero (or equal).