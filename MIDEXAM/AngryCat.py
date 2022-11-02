input_list = [int(x) for x in input().split(", ")]
index_start = int(input())
command = input()
left_list = input_list[:index_start]
right_list = input_list[index_start + 1:]

if command == "cheap":
    left_list = sum([x for x in left_list if x < input_list[index_start]])
    right_list = sum([x for x in right_list if x < input_list[index_start]])

elif command == "expensive":
    left_list = sum([x for x in left_list if x >= input_list[index_start]])
    right_list = sum([x for x in right_list if x >= input_list[index_start]])

if left_list >= right_list:
    print(f"Left - {left_list}")
else:
    print(f"Right - {right_list}")