'Tic tac toe'

firstline = input().split()
secondline = input().split()
thirdline = input().split()

condition1 = ((firstline[0] == secondline[0] == thirdline[0]) and firstline[0] == '1' or
              (firstline[1] == secondline[1] == thirdline[1]) and firstline[1] == '1' or
              (firstline[2] == secondline[2] == thirdline[2]) and firstline[2] == '1' or
              (firstline[0] == firstline[1] == firstline[2]) and firstline[0] == '1' or
              (secondline[0] == secondline[1] == secondline[2]) and secondline[0] == '1' or
              (thirdline[0] == thirdline[1] == thirdline[2]) and thirdline[0] == '1' or
              (firstline[0] == secondline[1] == thirdline[2]) and firstline[0] == '1' or
              (firstline[2] == secondline[1] == thirdline[0]) and firstline[2] == '1')

condition2 = ((firstline[0] == secondline[0] == thirdline[0]) and firstline[0] == '2' or
              (firstline[1] == secondline[1] == thirdline[1]) and firstline[1] == '2' or
              (firstline[2] == secondline[2] == thirdline[2]) and firstline[2] == '2' or
              (firstline[0] == firstline[1] == firstline[2]) and firstline[0] == '2' or
              (secondline[0] == secondline[1] == secondline[2]) and secondline[0] == '2' or
              (thirdline[0] == thirdline[1] == thirdline[2]) and thirdline[0] == '2' or
              (firstline[0] == secondline[1] == thirdline[2]) and firstline[0] == '2' or
              (firstline[2] == secondline[1] == thirdline[0]) and firstline[2] == '2')

if condition1:
    print("First player won")
elif condition2:
    print('Second player won')
else:
    print('Draw!')