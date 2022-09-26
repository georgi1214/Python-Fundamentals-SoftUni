name = input().split(', ')

result = sorted(name, key=lambda item: (-len(item), item))


print(result)