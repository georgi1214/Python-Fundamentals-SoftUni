def chat(message):
    for element in message:
        history_log.insert(len(history_log), element)


def delete(message):
    for element in message:
        if element in history_log:
            history_log.remove(element)


def edit(item_to_edit, edited_item):
    for index, element in enumerate(history_log):
        if element == item_to_edit:
            history_log[index] = edited_item


def pin(message):
    for element in message:
        for index, item in enumerate(history_log):
            if item == element:
                history_log.pop(index)
                history_log.insert(len(history_log), item)


def spam(message):
    for element in message:
        history_log.append(element)


command = input()
history_log = []
while True:
    if command == "end":
        break
    action = command.split()[0]
    rest_of_the_message = command.split(" ")[1::]

    if action == "Chat":
        chat(rest_of_the_message)
    if action == "Delete":
        delete(rest_of_the_message)
    if action == "Edit":
        item_to_edit = rest_of_the_message[0]
        edited_item = rest_of_the_message[1]
        edit(item_to_edit, edited_item)
    if action == "Pin":
        pin(rest_of_the_message)
    if action == "Spam":
        spam(rest_of_the_message)

    command = input()

print("\n".join(str(x) for x in history_log))