number = int(input())
wagons = [0] * number

while True:
    command = input()

    if command == "End":
        break

    data = command.split(' ')

    current_comand = data[0]

    if current_comand == 'add':
        peapole_to_add = data[1]
        wagons[-1] += int(peapole_to_add)
    elif current_comand == 'insert':
        index = int(data[1])
        number_of_peapole = int(data[2])
        wagons[index] += number_of_peapole
    elif current_comand == 'leave':
        index = int(data[1])
        number_of_peapole = int(data[2])
        wagons[index] -= number_of_peapole

print(wagons)