messages = []
commands = input()

while commands != 'end':
    command = commands.split()
    cmd = command[0]
    message = command[1]
    if cmd == 'Chat':
        messages.append(message)
    elif cmd == 'Delete':
        if message in messages:
            messages.remove(message)
    elif cmd == 'Edit':
        edit = command[2]
        for index, msg in enumerate(messages):
            if msg == message:
                messages[index] = edit
    elif cmd == 'Pin':
        for msg in messages:
            if msg == message:
                messages.remove(msg)
                messages.append(msg)
    elif cmd == 'Spam':
        k = 0
        for neshta in command:
            if k == 0:
                k += 1
                continue
            messages.append(neshta)

    commands = input()
for something in messages:
    print(something)