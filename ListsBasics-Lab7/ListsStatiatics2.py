number_of_numbers = int(input())

positive = []
positive_counter = 0
negative = []
negative_sum = 0

for i in range(number_of_numbers):
    numbers: int = int(input())
    if numbers >= 0:
        positive.append(numbers)
        positive_counter += 1

    if numbers < 0:
        negative.append(numbers)
        negative_sum = sum(negative)


print(positive)
print(negative)
print(f'Count of positives: {positive_counter}')
print(f'Sum of negatives: {negative_sum}')

