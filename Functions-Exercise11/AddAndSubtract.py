def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return (a + b) - c


result = 0

first_int = int(input())
second_int = int(input())
third_int = int(input())

result = subtract(first_int, second_int, third_int)


print(result)