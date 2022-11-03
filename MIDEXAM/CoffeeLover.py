coffee_list = input().split()
commands_qty = int(input())

for each in range(commands_qty):
    command = input().split()
    event = command[0]
    if event == "Include":
        coffee_sort = command[1]
        coffee_list.append(coffee_sort)
    elif event == "Remove":
        first_last = command[1]
        count = int(command[2])
        if len(coffee_list) > count:
            if first_last == "first":
                coffee_list = coffee_list[count:]
            elif first_last == "last":
                coffee_list = coffee_list[:len(coffee_list) - count]
    elif event == "Prefer":
        index_one = int(command[1])
        index_two = int(command[2])
        if 0 <= index_one < len(coffee_list) and 0 <= index_two < len(coffee_list) and index_one != index_two:
            coffee_list[index_one], coffee_list[index_two] = coffee_list[index_two], coffee_list[index_one]
    elif event == "Reverse":
        coffee_list = coffee_list[::-1]

print("Coffees:")