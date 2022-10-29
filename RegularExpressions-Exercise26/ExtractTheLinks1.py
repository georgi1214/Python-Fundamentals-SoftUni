import re

pattern = r'((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))'
text = input()
valids = []

while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        valids.append(match.group(1))
    text = input()

for valid in valids:
    print(valid)