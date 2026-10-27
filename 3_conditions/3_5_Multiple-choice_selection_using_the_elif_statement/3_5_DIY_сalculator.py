"""
Task: DIY Calculator

Description:
Write a program that reads two real numbers from the keyboard, followed by a string.
If this string represents one of the four basic mathematical operations (+, -, *, or /), output the result of applying that operation to the previously entered numbers; otherwise, output "Unknown".
You should also output "Unknown" if the user attempts to divide by zero.

Input data
Two real numbers, each on a separate line. The third line contains the operation symbol.

Output
You need to calculate the result of an operation: '+', '-', '*', or '/'. If a character is entered that does not correspond to one of these operations, you should output "Unknown".
"Unknown" should also be output if there is an attempt to divide by zero.

Input Example:
3.5
2.5
+

Output Example:
6.0
"""

a, b, s = float(input()), float(input()), input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/':
    if b == 0:
        print('Unknown')
    else:
        print(a / b)
else:
    print('Unknown')


