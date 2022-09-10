n = int(input())

positive = []
negative = []
counter = 0

for _ in range(n):
    num = int(input())
    if num >= 0:
        positive.append(num)
        counter += num
    if num < 0:
        negative.append(num)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(F'Sum of negatives: {sum(negative)}')


