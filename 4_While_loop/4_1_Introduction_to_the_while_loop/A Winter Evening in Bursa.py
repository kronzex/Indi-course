"""
Task: A Winter Evening in Bursa

Description:
Take a number. Multiply it by its own first digit. Then, multiply the result by the first digit of that new number, and so on. For example, starting with 8:

8→8∗8=64
64→6∗64=384
384→3∗384=1152
1152→1∗1152=1152

Clearly, once the first digit of a number in this sequence becomes 1, the numbers stop changing. However, this does not happen for every starting number.

Write a program that determines, at least approximately, the fate of a given number 'n'.

Starting with the number 'n', multiply the current number by its first digit—repeating this process until either the first digit of the resulting number becomes 1 or the number itself exceeds one billion. Output the final result.

Input Example:
223


Output Example:
1784

"""

n = int(input())

while True:
    # Get the first digit of the number
    first_digit = int(str(n)[0])

    # If the first digit is 1, output the result and exit.
    if first_digit == 1:
        print(n)
        break

    # We multiply
    n = n * first_digit

    # If it exceeds a billion — we cash out and exit.
    if n > 1_000_000_000:
        print(n)
        break






