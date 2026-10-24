"""
Task: Four-Digit Palindrome Check

Description:
Write a program to determine whether a given four-digit natural number N is a palindrome, meaning it reads the same from left to right as it does from right to left.

The program receives a positive four-digit integer N as input and must print "YES" if N is a palindrome, and "NO" otherwise.

Input Example:
4554

Output Example:
YES
"""

n = int(input())

# Extract individual digits of the number
digit_1 = n % 10          # Units digit
digit_2 = n % 100 // 10   # Tens digit
digit_3 = n % 1000 // 100 # Hundreds digit
digit_4 = n // 1000       # Thousands digit

# Check if the number is a palindrome (comparing outer digits: thousands with units, and hundreds with tens)
if digit_4 == digit_1 and digit_3 == digit_2:
    print('YES')
else:
    print('NO')