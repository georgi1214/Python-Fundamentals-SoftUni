def calculates(a, b, c):

    if a == 'multiply':
        return b * c

    elif a == 'divide':
        return int(b / c)

    elif a == 'add':
        return b + c

    elif a == 'subtract':
        return b - c


operator = input()
num1 = int(input())
num2 = int(input())


print(calculates(operator, num1, num2))