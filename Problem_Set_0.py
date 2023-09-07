'''
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”.
'''

import math

x = int(input("Enter a number 'x': "))
y = int(input("Enter a number 'y': "))

power = x ** y
log_value = math.log(x, 2)

print(x, "to the power of", y, "is", power)
print("log (base 2) of", x, "is", log_value)