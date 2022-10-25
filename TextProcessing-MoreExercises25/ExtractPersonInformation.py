def extract_info():
    n = int(input())
    for i in range(n):
        text = input()
        name = ''
        age = 0
        index_start_name = 0
        index_start_age = 0
        for index, ch in enumerate(text):
            if ch == '@':
                index_start_name = index + 1
            if ch == '|':
                index_end_name = index
                name = text[index_start_name:index_end_name]
            if ch == '#':
                index_start_age = index + 1
            if ch == '*':
                index_end_age = index
                age = text[index_start_age:index_end_age]
        print(f'{name} is {age} years old.')


extract_info()