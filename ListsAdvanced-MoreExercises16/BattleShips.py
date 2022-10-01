def attack(field, square):
    ships_destroyed = 0
    for att in square:
        turn = att.split('-')
        row = int(turn[0])
        column = int(turn[1])

        if field[row][column] > 0:
            field[row][column] -= 1
            if field[row][column] == 0:
                ships_destroyed += 1

    return ships_destroyed


rows = int(input())
fields = []
for _ in range(rows):
    temp_field = input().split()
    fields.append(list(map(int, ''.join(temp_field))))
square_attacked = input().split()
print(attack(fields, square_attacked))