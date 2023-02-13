def checkPalindrome(num):
    reverse = 0
    temp = num

    while (num > 0):
        r = num % 10
        num //= 10  # Reminder to use INTEGER DIVISION
        reverse = (reverse * 10) + r

    if (temp == reverse):
        return True
    else:
        return False

    pass


num = int(input())
isPalindrome = checkPalindrome(num)
if (isPalindrome):
    print('true')
else:
    print('false')
