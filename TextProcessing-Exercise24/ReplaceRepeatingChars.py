def replace_chars(text):
    new_string = ''
    char = ''
    for ch in text:
        if ch != char:
            new_string += ch
            char = ch
    return new_string


print(replace_chars(input()))