first_symbol = ord(input())
second_symbol = ord(input())
text = input()

total_sum = 0

for ch in text:
    if first_symbol < ord(ch) < second_symbol:
        total_sum += ord(ch)

print(total_sum)