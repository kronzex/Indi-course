"""
Task: Magnetic poles

Description:
When two magnets are placed near each other, they begin to interact. Like magnetic poles (north/north or south/south) repel each other, while opposite magnetic poles (north/south) attract each other.

Your program receives two values, each on a separate line, representing the polarities of the magnets—either 'N' (north) or 'S' (south).

Your task is to store the string "Attract" (Притягиваются) in the variable `experiment` if the magnets have opposite polarities; otherwise, store the string "Repel" (Отталкиваются).

Finally, output the value of the variable `experiment`.

Input Example:
N
N

Output Example:
Отталкиваются
"""

a, b = input(), input()
experiment = 'Притягиваются' if a != b else 'Отталкиваются'
print(experiment)




