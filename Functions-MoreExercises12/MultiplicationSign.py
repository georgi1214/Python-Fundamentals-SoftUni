first_num = int(input())
second_num = int(input())
third_num = int(input())

result = first_num * second_num * third_num

if result < 0:
    print('negative')
elif result > 0:
    print('positive')
elif result == 0:
    print('zero')