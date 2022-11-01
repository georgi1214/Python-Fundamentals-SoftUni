import re
participants = input().split(', ')
result_dict = {}
pattern = r'\w'

while True:
    data = input()
    if data == 'end of race':
        break

    result = re.findall(pattern, data)
    person_name = ''.join([ch for ch in result if ch.isalpha()])
    sum_nums = sum([int(digit) for digit in result if digit.isdigit()])

    if person_name in participants and person_name not in result_dict:
        result_dict[person_name] = sum_nums
    elif person_name in participants and person_name in result_dict:
        result_dict[person_name] += sum_nums
i = 1
result_dict = sorted(result_dict.items(), key=lambda x: -x[1])
for k, v in result_dict:
    if i == 4:
        break
    if i == 1:
        print(f'1st place: {k}')
    elif i == 2:
        print(f'2nd place: {k}')
    elif i == 3:
        print(f'3rd place: {k}')
    i += 1