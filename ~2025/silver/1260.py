#input = open('input.txt','r').readline #개인 확인용

#input = open('input.txt','r').readline  # 개인 확인용

from collections import deque

def dfs(v):
    visited_dfs[v] = True  # 방문 처리
    print(v, end=' ')
    for next_v in graph[v]:
        if not visited_dfs[next_v]:
            dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True  # 방문 처리
    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for next_v in graph[current]:
            if not visited_bfs[next_v]:
                visited_bfs[next_v] = True  # 방문 처리
                queue.append(next_v)

# 입력 처리
N, M, V = map(int, input().split())  # 정점의 개수 N, 간선의 개수 M, 시작 정점 V
graph = [[] for _ in range(N + 1)]  # 인접 리스트 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프

# 인접 리스트 오름차순 정렬
for adj in graph:
    adj.sort()

# 방문 리스트 초기화
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

# DFS 및 BFS 실행
dfs(V)
print()
bfs(V)

'''
백준 1260번 DFS와 BFS

문제:
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력:
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

출력:
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

예시:
    예시 입력1:
        4 5 1
        1 2
        1 3
        1 4
        2 4
        3 4
    
    예시 출력1:
        1 2 4 3
        1 2 3 4
'''