"""
Task: Vasya and the Socks

Description:
Vasya has n pairs of socks. Each morning, as he gets ready for school, Vasya puts on a pair of socks. In the evening, upon returning from school, he takes them off and throws them away.
Every m-th day (on days m, 2m, 3m, ...), his mother buys him one new pair of socks. She does this late in the evening, so Vasya cannot wear the new socks until the following day.
For how many consecutive days will Vasya have enough socks?

Input:
The input consists of a single line containing two integers $n$ and $m$ (1 <= n <= 100; 2 <= m <= 100), separated by a space.

Output:
Output a single integer — the answer to the problem.

Input Example:
9 3

Output Example:
13
"""

n, m = map(int, input().split())
days = 0
while n > 0:
    days += 1
    n -= 1

    if days % m == 0:
        n += 1
print(days)




