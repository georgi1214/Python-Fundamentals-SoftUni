import re

text = input()
pattern = r"\d+"
all_nums = []

while text:
    numbers = re.findall(pattern, text)
    all_nums.extend(numbers)

    text = input()

print(*all_nums)