string = input()
counter_n = int(input())

repeat_string = lambda a, b: a * b
result = repeat_string(string, counter_n)


print(result)