def multiply(first, second):
    return first * second
def divide(first, second):
    return int(first / second)
def add(first, second):
    return first + second
def subtract(first, second):
    return first - second

command = input()
first1 = int(input())
second2 = int(input())


if command == 'multiply':
    print(multiply(first1, second2))
elif command == 'divide':
    print(divide(first1, second2))
elif command == 'add':
    print(add(first1, second2))
elif command == 'subtract':
    print(subtract(first1, second2))