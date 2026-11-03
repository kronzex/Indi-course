"""
Task: Words and slices

Description:
You are given a word as input. Your task is to iterate through all its letters using a `while` loop and print each one in the following format:

"Current letter: <letter>"

As soon as you encounter the lowercase English letters "e" or "a," you must print the phrase "Aha! Found it," stop printing the letters, and exit the loop immediately.

If the word does not contain the letters "e" or "a," you should print the phrase "Printed all letters."

Input Example:
phrase


Output Example:
Current letter: p
Current letter: h
Current letter: r
Aha! Found it
"""

n = input()
while len(n) > 0:
    if n[0] == 'a' or n[0] == 'e':
        print('Aha! Found it')
        break
    print(f'Current letter: {n[0]}')
    n = n[1:]
else:
    print('Printed all letters')





