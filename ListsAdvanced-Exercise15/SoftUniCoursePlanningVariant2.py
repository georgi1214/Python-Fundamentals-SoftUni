data = input().split(', ')
command = input()
while not command == "course start":
    command = command.split(':')
    action = command[0]
    lesson = command[1]
    exercise = f'{lesson}-Exercise'
    if action == 'Add':
        if lesson not in data:
            data.append(lesson)
    elif action == 'Insert':
        index = int(command[2])
        if lesson not in data:
            data.insert(index, lesson)
    elif action == 'Remove':
        if lesson in data:
            data.remove(lesson)
            if exercise in data:
                data.remove(exercise)

    elif action == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]
        exercise1 = f'{lesson1}-Exercise'
        exercise2 = f'{lesson2}-Exercise'
        if lesson1 in data and lesson2 in data:
            index1 = data.index(lesson1)
            index2 = data.index(lesson2)
            data[index1], data[index2] = data[index2], data[index1]

        if exercise2 in data:
            data.remove(exercise2)
            data.insert(data.index(lesson2) + 1, exercise2)

        elif exercise1 in data:
            data.remove(exercise1)
            data.insert(data.index(lesson1) + 1, exercise1)

    elif action == 'Exercise':
        if lesson in data:
            if exercise not in data:
                lesson_index = data.index(lesson)
                data.insert(lesson_index + 1, exercise)
        else:
            data.append(lesson)
            data.append(exercise)

    command = input()

for el in range(1, len(data) + 1):
    print(f'{el}.{data[el - 1]}')