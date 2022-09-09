key = int(input())
n = int(input())
message = []
for i in range(n):
    character = input()
    ord_plus_key = ord(character) + key
    ord_in_character = chr(ord_plus_key)
    message.append(ord_in_character)
print(''.join(message))