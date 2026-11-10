"""
Task: Minimal Divisor

Description:
The program receives a natural number n > 1 as input. Output the smallest divisor of this number, other than one.

For example, the divisors of the number 12 are 1, 2, 3, 4, 6, and 12.

Input Example:
997


Output Example:
997
"""


count = 2
if (n := int(input())) > 1:
    while n > count:
        if n % count == 0:
            print(count)
            break
        count += 1
    else:
        print(n)
else:
    print(1)




