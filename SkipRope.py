text = input()
numbers_list = [int(num) for num in text if num.isdigit()]
non_numbers = [ch for ch in text if not ch.isdigit()]
take_list = [ch for i, ch in enumerate(numbers_list) if i % 2 == 0]
skip_list = [ch for i, ch in enumerate(numbers_list) if i % 2 != 0]
result_string = ''
skipped_string = ''

for i in range(1, len(take_list) + 1):
    num1 = take_list[i - 1]
    num2 = skip_list[i - 1]
    for j in range(num1):
        if j >= len(non_numbers):
            break
        result_string += non_numbers[j]
    non_numbers = non_numbers[num1:]
    for j in range(num2):
        if j >= len(non_numbers):
            break
        skipped_string += non_numbers[j]
    non_numbers = non_numbers[num2:]

print(result_string)