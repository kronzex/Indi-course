"""
Task: Average exchange rate over three days

Description:
In a program that calculates the average currency exchange rate over the last three days:

Input data:

Three floating-point numbers (the exchange rate for three days) on separate lines.

Output data:

The program calculates the average exchange rate over the last three days and outputs the text in the following format:

<<Средний курс доллара за последние три дня: <средний курс> RUB.>>

where the average rate result is rounded to two decimal places.


Input Example:
96.50
97.25
95.80

Output Example:
Средний курс доллара за последние три дня: 96.52 RUB.
"""

# Solution:
day_1 = float(input())
day_2 = float(input())
day_3 = float(input())
average = (day_1 + day_2 + day_3) / 3
text = "Средний курс доллара за последние три дня: %.2f RUB." % (average)
print(text)




