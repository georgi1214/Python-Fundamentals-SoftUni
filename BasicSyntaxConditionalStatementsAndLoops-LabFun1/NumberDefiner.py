num = float(input())

if num == 0:
    print('zero')
elif num < 1 and num > 0:
    print('small positive')
elif num > 1000000:
    print('large positive')
elif num < -1000000:
    print('large negative')
elif num < -1:
    print('negative')
elif num > 1:
    print('positive')
elif num > -1 and num < 0:
    print('small negative')