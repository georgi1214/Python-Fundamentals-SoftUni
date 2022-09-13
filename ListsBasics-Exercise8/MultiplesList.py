factor = int(input())
count = int(input())

list_of_num = []

for multiplier in range(1, count + 1):
    list_of_num.append(factor * multiplier)
print(list_of_num)