integers = input()

A = integers.split(", ")
B = []

for char in A:
    if char == "0":
        A.remove(char)
        A.append(char)

for num in A:
    num = int(num)
    B.append(num)

print(B)