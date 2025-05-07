#input = open('input.txt','r').readline #개인 확인용

def floydWarshall(graph):
    length = len(graph)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if graph[j][k] == 0 or graph[j][k] == 1:
                    continue
                elif graph[j][k] > graph[j][i] + graph[i][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]

member = int(input())
graph = [[float('inf') for _ in range(member)] for _ in range(member)]

for i in range(member):
    graph[i][i] = 0

while True:
    m1, m2 = map(int, input().split())
    if m1 == -1 and m2 == -1:
        break
    graph[m1-1][m2-1] = 1
    graph[m2-1][m1-1] = 1

#print(graph)
floydWarshall(graph)
#print(graph)

#리스트 result를 새로 만들어  graph 배열들 안에 가장 큰 값 들을 result에 추가
result = []
for i in range(len(graph)):
    result.append(max(graph[i]))
    
captain = min(result)
#result에 가장 작은 값 과 몇개가 있는 지 출력
print(captain, result.count(captain))


#result의 가장 작은 값을 가지고 있는 것들 출력
for i in range(len(result)):
    if result[i] == captain:
        print(i+1, end=' ')

'''
백준 2660 회장뽑기

입력
입력의 첫째 줄에는 회원의 수가 있다. 단, 회원의 수는 50명을 넘지 않는다. 둘째 줄 이후로는 한 줄에 두 개의 회원번호가 있는데,
이것은 두 회원이 서로 친구임을 나타낸다. 회원번호는 1부터 회원의 수만큼 붙어 있다. 마지막 줄에는 -1이 두 개 들어있다.

출력
첫째 줄에는 회장 후보의 점수와 후보의 수를 출력하고, 두 번째 줄에는 회장 후보를 오름차순으로 모두 출력한다.

예제 입력:
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

예제 출력:
2 3
2 3 4
'''