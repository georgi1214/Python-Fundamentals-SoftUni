text = input()
modified_text = ''

for char in text:
    char = ord(char) + 3
    modified_text += chr(char)

print(modified_text)