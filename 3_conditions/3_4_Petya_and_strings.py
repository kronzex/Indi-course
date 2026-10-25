"""
Task: Magnetic poles

Description:
Little Petya really loves gifts. For his birthday, his mother gave him two strings of equal length, consisting of uppercase and lowercase Latin letters.
Now, Petya wants to compare these strings lexicographically. The case of the letters does not matter—that is, an uppercase letter is considered equivalent to its corresponding lowercase letter.
Help Petya perform this comparison.

Input:
Each of the first two lines contains a given string. The length of the strings is between 1 and 100, inclusive.
It is guaranteed that the strings have the same length and consist of uppercase and lowercase Latin letters.

Output
If the first string is lexicographically smaller than the second, output "-1". If the second string is lexicographically smaller than the first, output "1".
If the strings are equal, output "0". Note that the comparison is case-insensitive.

Input Example:
abs
Abz

Output Example:
-1
"""

a, b = input().lower(), input().lower()
if a == b:
    print(0)
else:
    if b < a:
        print(1)
    else:
        print(-1)





