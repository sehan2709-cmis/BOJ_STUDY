count = int(input())

for i in range(count):
    bracket = input()
    brackets = list(bracket)
    calculate = 0
  
    for j in brackets:
        if j == '(':
            calculate += 1
        elif j == ')':
            calculate -= 1
          
        if calculate < 0:
            print('NO')
            break
          
    if calculate > 0:
        print('NO')
    elif calculate == 0:
        print('YES')