n = int(input())
array = [0] * 5

for i in range(n):
    x, y = map(int, input().split())
    if(x*y == 0):
        array[0] += 1
    elif(x > 0 and y > 0):
        array[1] += 1
    elif(x < 0 and y > 0):
        array[2] += 1
    elif(x < 0 and y < 0):
        array[3] += 1
    else:
        array[4] += 1

print("Q1:", array[1])
print("Q2:", array[2])
print("Q3:", array[3])
print("Q4:", array[4])
print("AXIS:", array[0])

'''
 백준 9610번 사분면면
 n만큼의 점의 개수를 확인하여 각 사분면과 축에 점이 몇개 있는지 출력
 

백준 예시 입력값: 
5
0 0
0 1
1 1
3 -3
2 2

백준 예시 출력값: 
Q1: 2
Q2: 0
Q3: 0
Q4: 1
AXIS: 2
'''