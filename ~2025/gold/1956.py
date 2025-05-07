#input = open('input.txt','r').readline #개인 확인용



V, E = map(int, input().split())

graph = [[float('inf') for _ in range(V)] for _ in range(V)]

print(graph)
#for i in range(E):
#   print("a")
    
'''
백준 1956 운동

입력
첫째 줄에 V와 E가 빈칸을 사이에 두고 주어진다. (2 ≤ V ≤ 400, 0 ≤ E ≤ V(V-1))
다음 E개의 줄에는 각각 세 개의 정수 a, b, c가 주어진다.

a번 마을에서 b번 마을로 가는 거리가 c인 도로가 있다는 의미이다.
(a → b임에 주의) 거리는 10,000 이하의 자연수이다.
(a, b) 쌍이 같은 도로가 여러 번 주어지지 않는다.

출력
첫째 줄에 최소 사이클의 도로 길이의 합을 출력한다. 운동 경로를 찾는 것이 불가능한 경우에는 -1을 출력한다.

예제 입력:
3 4
1 2 1
3 2 1
1 3 5
2 3 2

예제 출력:
3
'''