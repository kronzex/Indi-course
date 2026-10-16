"""
Task: Float Number Check

Description:
Your task is to write a program that checks whether an input string can be converted to a floating-point number. Both a dot and a comma can be used as the separator between the integer and fractional parts.

Examples of values that can be converted:
- 456
- 123.56
- 18,9

Examples of values that cannot be converted:
- 456.32.23
- 54,32

If the check passes, output the message "Можно преобразовать", otherwise output "Нельзя преобразовать[span_11](start_span)"[span_11](end_span).

Input Example:
24.32

Output Example:
Можно преобразовать
"""

s = input().strip()

# Replace comma with dot for uniformity
s = s.replace(',', '.')

# Check that the string contains only digits and at most one dot
if s.count('.') > 1:
    print("Нельзя преобразовать")
else:
    # Remove the dot and check that everything else consists of digits
    temp = s.replace('.', '')
    if temp.isdigit():
        print("Можно преобразовать")
    else:
        print("Нельзя преобразовать")