"""
Task: String Task

Description:
Petya started learning programming. In his first lesson, he was given a task to write a program.
Given a string consisting of uppercase and lowercase Latin letters, the program must:
1. Delete all vowels ('A', 'O', 'Y', 'E', 'U', 'I').
2. Insert a '.' symbol before each consonant letter.
3. Replace all uppercase consonant letters with lowercase ones.

The program receives exactly one string as input and must return the processed string as output.

Input Example:
Codeforces

Output Example:
.c.d.f.r.c.s
"""


n = input()
n_a = n.replace('A','').replace('a','').replace('O','').replace('o','').replace('Y','').replace('y','').replace('E','').replace('e','').replace('U','').replace('u','').replace('I','').replace('i','').lower()
n_b = n_a.replace('', '.')
print(n_b.rstrip('.'))






