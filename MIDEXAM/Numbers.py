sequence = list(map(int, input().split()))

while True:
    commands = input()
    if commands != 'Finish':
        commands = commands.split()
        command = commands[0]
        value = int(commands[1])

        if command == 'Add':
            sequence.append(value)

        elif command == 'Remove':
            for thing in sequence:
                if value == thing:
                    sequence.remove(value)
                    break

        elif command == 'Replace':
            replacement = int(commands[2])
            for index, thing in enumerate(sequence):
                if value == thing:
                    sequence[index] = replacement
                    break

        elif command == 'Collapse':
            sequence = [x for x in sequence if x >= value]
        else:
            continue
    else:
        print(*sequence, sep=' ')