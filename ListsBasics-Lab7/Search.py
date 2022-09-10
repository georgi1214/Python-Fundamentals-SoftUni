n = int(input())
word = input()

string = []

for number in range(n):
    text = input()
    string.append(text)
print(string)
for number in range(len(string) -1, -1, -1):
    element = string[number]
    if word not in element:
        string.remove(element)
print(string)


