"""
Task: Воронеж! 'ж' for you

Description:
In the game of "Cities," players take turns naming cities such that the first letter of each new word matches the last letter of the previous one. 
If the last letter of the previous word is a "soft sign" (ь), the first letter of the next word must instead match the letter that precedes the soft sign.
Write a program that reads two consecutive strings and outputs "Good" if the last character of the first string matches the first character of the second string (taking the soft sign rule into account), or "Bad" otherwise.


Input Example:
Лондон
Норильск

Output Example:
Good
"""

n, y = input().lower().rstrip('ь'), input().lower().rstrip('ь')
if n[-1] == y[0]:
    print('Good')
else:
    print('Bad')








