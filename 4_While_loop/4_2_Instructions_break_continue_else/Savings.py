"""
Task: Savings

Description:
You are saving money to reach a specific goal. You have a list of income amounts, and you want to:

    ✔️  Accumulate a total by adding up these income amounts in order;

    ✔️  Determine whether or not the target amount has been reached.

Write a program that:

    ✔️ Takes a list of numbers (income amounts) as input—separated by spaces on a single line—followed by the target amount on the next line;

    ✔️ Adds the numbers from the list in order, using a `while` loop;

    ✔️ Stops the process as soon as the accumulated sum becomes greater than or equal to the target amount;

    ✔️ Outputs the final accumulated sum and, on a separate line, the message:

        ➖ "Goal reached" if the final sum is greater than or equal to the target amount.

        ➖ "The goal has not been reached" if the list has been exhausted, yet the total remains less than the target amount.

Input Example:
10 20 15
10


Output Example:
10
Цель достигнута
"""


incoming = list(map(int, input().split()))
goal = int(input())

total = 0
ind = 0

while ind < len(incoming):
    total += incoming[ind]
    if total >= goal:
        print(total)
        print('Goal reached')
        break
    ind += 1
else:
    print(total)
    print('The goal has not been reached')







