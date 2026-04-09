
'''
코드 풀이 과정
    #내가 처음에 작성한 코드
    로프가 예를 들어 1kg, 10kg, 100000kg를 감당 가능한 로프들이 있다면.
    1kg를 사용 할때는 최대 3kg
    10kg를 사용 할때는 최대 20kg
    100000kg를 사용 할때는 100000kg
    가 가능 할테니 꼭 가장 가벼운 무게를 사용해서 곱하기를 하는게 좋지는 않아 보임.

    #값 받기
    length = int(input())
    ropes = list()
    for i in range(length):
        ropes.append(int(input()))

    #리스트[가벼움 -> 무거움]로 정리
    ropes.sort()

    #인덱스 값 x (리스트 length - index) 하면 총 무게 감당 가능 값 나옴
    for i in range(length):
        ropes[i] = ropes[i] * (length - i)

    #리스트[무거움 -> 가벼움]으로 다시 정리
    #리스트[0] 값 보내면 된다.
    ropes.sort(reverse=True)
    print(ropes[0])

    #다른 사람 제출 답안 1
    
    #다른 사람 제출 답안 2

    #"내 코드 vs 다른 사람" 배울 점은?
'''
length = int(input())
ropes = list()
for i in range(length):
    ropes.append(int(input()))

ropes.sort()

for i in range(length):
    ropes[i] = ropes[i] * (length - i)

ropes.sort(reverse=True)
print(ropes[0])
#다시 짠 코드

'''
로프 (그리디)
난이도: 실버 4
시간 제한: 2초
메모리 제한: 192MB 
기출: 백준 https://www.acmicpc.net/problem/2217

문제:
    N(1 ≤ N ≤ 100,000)개의 로프가 있다. 이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다.
    각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

    하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다.
    k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

    각 로프들에 대한 정보가 주어졌을 때, 이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
    모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

입력 조건:
    첫째 줄에 정수 N이 주어진다. 다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 이 값은 10,000을 넘지 않는 자연수이다.

출력 조건:
    첫째 줄에 답을 출력한다.

입력 예시 1:
    2
    10
    15

출력 예시 1:
    20
'''