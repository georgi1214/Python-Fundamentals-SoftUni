num_lines = int(input())
capacity = 255
water_counter = 0

for line in range(num_lines):
    liters_water = int(input())
    if capacity - liters_water < 0:
        print('Insufficient capacity!')
        continue
    water_counter += liters_water
    capacity -= liters_water
print(water_counter)
