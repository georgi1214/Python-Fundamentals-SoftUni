def int_function(b):
    return b * 2

def real_function(b):
    return b * 1.5

def string_function(b):
    return b

string = input()
int_num = input()

if string == 'int':
    print(int_function(int(int_num)))
elif string == 'real':
    print(f'{real_function(float(int_num)):.2f}')
elif string == 'string':
    print(f'${string_function(str(int_num))}$')