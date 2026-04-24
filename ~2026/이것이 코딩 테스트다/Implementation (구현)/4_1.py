#두 번째 코드
n = int(input())
plans = input().split()
x, y = 1, 1

# 이동 규칙을 딕셔너리로 정의 (dx, dy)
move_rules = {
    'L': (0, -1), 'R': (0, 1),
    'U': (-1, 0), 'D': (1, 0)
}

for plan in plans:
    # 1. 일단 이동해보기
    dx, dy = move_rules[plan]
    nx, ny = x + dx, y + dy
    
    # 2. 범위를 벗어나는지 체크
    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny  # 유효할 때만 갱신

print(x, y)

'''
교재 답안 예시:
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move types = ['L', 'R'', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)

---------
1. 내 코드 vs 교재 답안 비교
   - 내 코드: if-elif 문으로 직접 이동 (직관적이지만 코드가 길어짐)
   - 교재: dx, dy (방향 벡터) 리스트 활용 (확장성이 좋고 알고리즘 정석 방식)

2. 핵심 피드백 (Best Practice)
   - '방향 벡터' 활용: dx = [0, 0, -1, 1], dy = [-1, 1, 0, 0] 처럼 이동량을 미리 정의
   - '선 검증 후 이동': 일단 다음 좌표(nx, ny)를 계산해보고, 격자를 안 벗어날 때만 실제 좌표(x, y)를 갱신
   - 가독성: 딕셔너리(dict)를 쓰면 if-elif 없이 한 줄로 이동 로직 처리가 가능


내 첫 코드:
N = int(input())
A = input().split(" ")

now = [1, 1]

def move(char):
    if char == 'L' and now[1] > 1:
        now[1] -= 1
    elif char == 'R' and now[1] < N:
        now[1] += 1
    elif char == 'U' and now[0] > 1:
        now[0] -= 1
    elif char == 'D' and now[0] < N:
        now[0] += 1

for i in A:
    move(i)

print(*now)
'''

'''
[문제 상화좌우]
구현
난이도 하
풀이 시간 15분
시간 제한 1초
메모리 제한 128 MB

문제
    여행가 A는 N x N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있다.
    계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀있다. 각 문자의 의미는 다음과 같다.
        - L: 왼쪽으로 한 칸 이동
        - R: 오른쪽으로 한 칸 이동
        - U: 위로 한 칸 이동
        - D: 아래로 한 칸 이동
    이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.

입력 조건
    - 첫째 줄에 크기를 나타내는 N이 주어진다 ( 1 <= N <= 100)
    - 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)

출려 조건
    - 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.
'''