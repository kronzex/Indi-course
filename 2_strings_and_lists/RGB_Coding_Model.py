''' Task: RGB Coding Model

Description:
Write a program that converts RGB color values into a hexadecimal color code representation.

The model uses three base colors: Red, Green, and Blue, with values ranging from 0 to 255.
Each color in the RGB model is formatted as #RRGGBB, where:
1. It starts with a # symbol.
2. Followed by two characters for the red color shade in hexadecimal format.
3. Followed by two characters for the green color shade in hexadecimal format.
4. Followed by two characters for the blue color shade in hexadecimal format.

The program receives 3 integers as input, each on a separate line:
* Red shade value
* Green shade value
* Blue shade value
*(Values range from 0 to 255 inclusive).*

The program must return the resulting hexadecimal color string in uppercase as output.

---

Input Example:
75
0
130

Output:
#4B0082
'''

a = hex(int(input()))
b = hex(int(input()))
c = hex(int(input()))

a_string = str(a).lstrip("0x").zfill(2)
b_string = str(b).lstrip("0x").zfill(2)
c_string = str(c).lstrip("0x").zfill(2)
print("#", a_string.upper(), b_string.upper(), c_string.upper(), sep = "")




