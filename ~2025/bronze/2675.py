#T값 = 몇개의 케이스 ( 1 <= T <= 1000 랜덤값)

#T수 많큼 반복문
#R반복 횟수 받고
#S 각 char R만큼 반복 + 줄 바꿈 없음

#줄넘김 해야함*

T = int(input())

for i in range(T):
    R, S = input().split()
    for j in S:
        print(j*int(R), end='')
    print()