def index_calculation(input_command, max_index, previous_index):
    jump = int(input_command.split()[1])
    if previous_index + jump >= max_index:
        current_index = 0
    else:
        current_index = jump + previous_index
    previous_index = current_index

    return current_index, previous_index


def love_spreading(all_neighbours, current_index):
    msg = ''
    if all_neighbours[current_index] == 0:
        msg = f"Place {current_index} already had Valentine's day."
    else:
        all_neighbours[current_index] -= 2
        if all_neighbours[current_index] == 0:
            msg = f"Place {current_index} has Valentine's day."

    return all_neighbours, msg


neighborhood = list(map(int, input().split("@")))
command = input()
max_index_value = len(neighborhood)
past_index = 0
while True:
    if command == "Love!":
        break

    elif command.startswith("Jump"):
        index, past_index = index_calculation(command, max_index_value, past_index)
        neighborhood, message = love_spreading(neighborhood, index)
        if message != '':
            print(message)
        # if sum(neighborhood) == 0:
        #     break
    command = input()

print(f"Cupid's last position was {past_index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    failed_houses = len(neighborhood) - neighborhood.count(0)
    print(f"Cupid has failed {failed_houses} places.")