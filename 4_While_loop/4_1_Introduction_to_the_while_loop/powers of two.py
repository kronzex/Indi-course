"""
Task: powers of two

Description:
In computer architecture, numbers that are powers of two: 1, 2, 4, 8, and so on—play an important role. Write a program that checks whether a given natural number is a power of two.
If it is, output the power itself; otherwise, output "NO".


Input Example:
8
Output Example:
3
"""

a = int(input())
degree = 0

while 2 ** degree < a:
    degree += 1

if 2 ** degree == a:
    print(degree)
else:
    print("NO")







