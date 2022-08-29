num = int(input())

for _ in range(num):
    code = int(input())
    if code == 88:
        print('Hello')
    elif code == 86:
        print('How are you?')
    elif code < 88 and code < 86:
        print('GREAT!')
    elif code == 87:
        print('GREAT!')
    elif code > 88:
        print('Bye.')
