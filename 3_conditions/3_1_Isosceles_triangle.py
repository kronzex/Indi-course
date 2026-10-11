"""
Task: Isosceles Triangle Check

Description:
Three natural numbers a, b, and c are given on separate lines. Your task is to determine whether the triangle is isosceles.

The program must output:
- "YES" if the given sides form an isosceles triangle;
- "NO" if the triangle is not isosceles or does not exist.

Input Example:
5
4
5

Output Example:
YES
"""

a, b, c = int(input()), int(input()), int(input())

# Check for triangle inequality theorem (validity of the triangle)
if a + b > c and c + b > a and a + c > b:
    # Check if the triangle is isosceles (at least two sides are equal)
    if a == b and a != c:
        print('YES')
    elif a == c:
        print('YES')
    elif c == b:
        print('YES')
    else:
        print('NO')
else:
    print('NO')