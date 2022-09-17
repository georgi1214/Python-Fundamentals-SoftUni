def calculates_order(a, b):

    if a == 'coffee':
        return b * 1.50

    elif a == 'water':
        return b * 1.00

    elif a == 'coke':
        return b * 1.40

    elif a == 'snacks':
        return b * 2.00


product = input()
count_of_products = int(input())

print(f'{calculates_order(product, count_of_products):.2f}')