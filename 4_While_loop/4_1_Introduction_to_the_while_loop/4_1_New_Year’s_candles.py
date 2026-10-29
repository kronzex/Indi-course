"""
Task: New Year’s candles

Description:
Vasily the programmer is a romantic at heart; for this New Year’s, he has decided to illuminate his room using candles.

Vasily has 'a' candles. When he lights a new candle, it burns for exactly one hour before going out. Being a clever fellow, Vasily knows how to craft one new candle out of 'b' used-up (extinguished) candles.
This new candle—just like any other—can then be lit.

Now, Vasily wants to know the total number of hours his candles can provide light, assuming he acts in the most efficient way possible. Help him find this number.

Input:
The single line contains two integers a and b (1 ≤ a ≤ 1000; 2 ≤ b ≤ 1000).

Output:
Output a single integer — the number of hours Vasily will be able to light the room.

Input Example:
4 2

Output Example:
7
"""

a, b = map(int, input().split())
hour = 0

while a > 0:
    hour += 1
    a -= 1
    if hour % b == 0:
        a += 1
print(hour)







