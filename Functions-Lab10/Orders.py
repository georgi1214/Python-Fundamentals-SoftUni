def calculate_total_price(product1, count_of_products1):
    return product1 * count_of_products1
price = 0

product = input()
count_of_product = int(input())

coffee = 1.50
water = 1.00
coke = 1.40
snacks = 2.00

if product == 'coffee':
    price = calculate_total_price(coffee, count_of_product)
elif product == 'water':
    price = calculate_total_price(water, count_of_product)
elif product == 'coke':
    price = calculate_total_price(coke, count_of_product)
elif product == 'snacks':
    price = calculate_total_price(snacks, count_of_product)
print(f'{price:.2f}')