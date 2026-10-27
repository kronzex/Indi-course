"""
Task: Pay Taxes

Description:
Income tax exists in all countries. In some countries it is higher, in others it is lower. In Russia, citizens pay an income tax of 13%.
Now imagine that people with an income of less than 20,000 rubles are exempt from paying tax.
Write a program that receives an income value as an integer input and displays the amount remaining after paying the 13% tax. If a person's salary is less than 20,000 rubles, tax is not withheld.

Input Example:
10000

Output Example:
10000
"""

n = int(input())
if n < 20000:
    print(n)
else:
    percent = n * 0.13
    n = n - percent # we deduct the percentage
    print(n)




