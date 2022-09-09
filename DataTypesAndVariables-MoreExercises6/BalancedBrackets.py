lines_count = int(input())
expression = []
open_braket = False
brakets = []
for i in range(lines_count):
    current_line = input()
    if current_line in ("(", ")"):
        brakets.append(current_line)
    expression.append(current_line)

open_brkets = expression.count("(")
closed_brekets = expression.count(")")
list_2_string = "".join(expression)
nested_brekets = list_2_string.count("((")

if brakets[0] == "(":
    open_braket = True
if (open_brkets == closed_brekets) and nested_brekets == 0 and open_braket:
    print("BALANCED")
else:
    print("UNBALANCED")