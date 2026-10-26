"""
Task: Petya and the Cake

Description:
For his birthday, Petya bought a beautiful and delicious cake that was perfectly circular in shape.
Since Petya did not know how many guests would attend his birthday party, he had to come up with an algorithm to quickly cut the cake into N equal pieces.
Note that cuts can be made either along a radius or along a diameter.
Help Petya solve this problem by determining the minimum number of cuts required to divide the cake for a given number of guests.

Input:
The program receives a natural number N as input—the number of guests, including the birthday celebrant himself.

Output:
Output the minimum possible number of cuts required for the cake.

Input Example:
2

Output Example:
1
"""

n = int(input())
if n > 1:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n)
else:
    print(0)


