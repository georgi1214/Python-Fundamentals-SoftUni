letters = input().split(", ")
letter_and_digits = {letters[i]: ord(letters[i]) for i in range(len(letters))}
print(letter_and_digits)