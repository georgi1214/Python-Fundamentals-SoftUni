name = 0

command = 0

while True:
    name = input()
    command = len(name)

    if name == 'Voldemort':
        print("You must not speak of that name!")
        break
    elif name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    elif command < 5:
        print(f"{name} goes to Gryffindor.")

    elif command == 5:
        print(f'{name} goes to Slytherin.')

    elif command == 6:
        print(f"{name} goes to Ravenclaw.")

    elif command > 6:
        print(f"{name} goes to Hufflepuff.")

