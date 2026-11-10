"""
Task: Collatz Conjecture

Description:
The Syracuse sequence, also known as the Collatz sequence, is constructed as follows: take a natural number 'n'; if it is even, replace it with 'n/2';
if it is odd, replace it with '3n+1'. The resulting number is the next term in the Syracuse sequence after 'n'. Then, apply the same rule to the new number, and so on.

Determine how many steps it takes for a Syracuse sequence, starting from a given number, to reach 1.

Typically, if you repeat this process enough times, you eventually arrive at the number 1 (which is then followed by 1 again). For example:

8 → 4 → 2 → 1 or 10 → 5 → 16 → 8 → 4 → 2 → 1.

Input Example:
10


Output Example:
6
"""


n = int(input())
count = 0

while n != 1:
    if n % 2 == 0:
        n //= 2      # integer division
    else:
        n = n * 3 + 1
    count += 1

print(count)






