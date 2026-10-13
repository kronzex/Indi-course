"""
Task: Lucky Ticket

Description:
Do you use public transport? You probably paid your fare and received a ticket with a number. A ticket is called lucky if it has a six-digit number (sometimes with leading zeros) where the sum of the first three digits is equal to the sum of the last three digits. That is, tickets with numbers 385916 and 2011 are lucky, since 3+8+5=9+1+6 and 0+0+2=0+1+1. You need to write a program that checks whether a ticket is "lucky".

The program receives a single integer N (0 <= N < 10^6) as input and must print "YES" if the ticket with number N is lucky, and "NO" otherwise.

Input Example:
385916

Output Example:
YES
"""

n = int(input())

# Extract individual digits of the number
digit_1 = n % 10            # Units digit
digit_2 = n % 100 // 10     # Tens digit
digit_3 = n % 1000 // 100   # Hundreds digit
digit_4 = n % 10000 // 1000 # Thousands digit
digit_5 = n % 100000 // 10000 # Ten-thousands digit
digit_6 = n // 100000       # Hundred-thousands digit

# Check if the sum of the first three digits equals the sum of the last three digits
if digit_1 + digit_2 + digit_3 == digit_4 + digit_5 + digit_6:
    print('YES')
else:
    print('NO')