"""
Task: Character Codes (Коды символов)

Description:
Write a program that takes three space-separated characters as input
and prints their character codes using the ord() function.

Format:
Код символа <symbol> равен <code_value>

Input Example:
A B C

Output Example:
Код символа A равен 65
Код символа B равен 66
Код символа C равен 67
"""

# Solution:
a, b, c = input().split()

print(f"Код символа {a} равен {ord(a)}")
print(f"Код символа {b} равен {ord(b)}")
print(f"Код символа {c} равен {ord(c)}")