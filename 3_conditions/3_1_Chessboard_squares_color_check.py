"""
Task: Chessboard Squares Color Check

Description:
Write a program that takes the coordinates of two squares on a chessboard as input and outputs a message stating whether they are of the same color. Columns on the chessboard are denoted by lowercase English letters.

The program must output "YES" if the squares are of the same color, and "NO" if they are of different colors. It is guaranteed that the column values are the Latin letters "abcdefgh", and the row values are digit symbols from 1 to 8.

Input Example:
a1
b2

Output Example:
YES
"""

s = 'abcdefgh'
inp = input()
inp_2 = input()

# Convert letter column to a numeric index
part_inp = inp[0]
part_inp_2 = inp_2[0]

column = s.find(part_inp)
column_2 = s.find(part_inp_2)

# Find the row number
row = int(inp[1])
row_2 = int(inp_2[1])

# Check if both cells have the same color based on the parity of their coordinates sum
if (column + row) % 2 == 0 and (column_2 + row_2) % 2 == 0 or (column + row) % 2 == 1 and (column_2 + row_2) % 2 == 1:
    print('YES')
else:
    print('NO')