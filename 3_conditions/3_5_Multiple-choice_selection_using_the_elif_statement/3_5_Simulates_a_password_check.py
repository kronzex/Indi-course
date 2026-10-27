"""
Task: simulates a password check

Description:
Write a program that simulates the verification of a password created by a user. The user first enters a password, then enters it again for confirmation. You need to handle the following scenarios:

   ➖ if the password entered by the user (the first time) is shorter than 7 characters, the program outputs "Short";

   ➖ if the password is long enough, but the password entered the second time does not match the first one, the program outputs "Difference";

   ➖ if this check is also passed successfully, the program outputs "OK".

Input Example:
qwerty123
qwerty

Output Example:
Difference

"""

a, b = input(), input()
if len(a) < 7:
    print('Short')
elif a[:] != b[:]:
    print('Difference')
else:
    print('OK')






