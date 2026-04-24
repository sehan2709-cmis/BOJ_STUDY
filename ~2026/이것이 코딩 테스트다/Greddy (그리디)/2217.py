
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

    ---
    #다른 사람 제출 답안 1
    #출처: https://hongcoding.tistory.com/26
    n = int(input())
    rope = []

    for i in range(n):
        rope.append(int(input()))
    rope.sort(reverse=True)

    for i in range(n):
        rope[i] = rope[i] * (i+1)

    print(max(rope))

    생각 정리:
        여기 에시는 구지 소팅을 한번더 하기 보다는 그냥 max()를 사용했다.
        이걸 왜 생각을 못했을까... 일단 근데 방법은 크게 다르지 않다.
    
    ---
    #다른 사람 제출 답안 2
    #출처: https://star7sss.tistory.com/397

    import sys
    input = sys.stdin.readline

    # 입력
    N = int(input())
    rope = []
    for _ in range(N):
        rope.append(int(input()))

    # 내림차순 정렬
    rope.sort(reverse=True)

    # 그리디 알고리즘
    res = 0
    for k, w in enumerate(rope, 1):
        res = max(res, w*k)
    print(res)

    생각 정리:
        전체 적인 큰 그림은 크게 다르지 않다.
        하지만 마지막에 첫번째 예시 혹은 나와는 다르게
        내림차순으로 정리한 것과 for range보다는 "enumerate"를 사용한 걸 볼 수 있다.
        구지 빼기를 추가하거나 추후에

    #"내 코드 vs 다른 사람" 배울 점은?
    1. enumerate 쓰니까 인덱스 따로 안 더해도 되고 코드가 훨씬 직관적이라 편함.
    2. 리스트에 다 채워놓고 max 돌리는 것보다 실시간으로 갱신하는 게 메모리도 아끼고 더 효과적임.
      - 기존 방식처럼 모든 계산 결과를 리스트에 저장한 뒤 max()를 호출하면 리스트 크기만큼의 추가 메모리(공간 복잡도 O(N))가 필요
      - 반면, 변수 하나(res)에 실시간으로 최댓값을 갱신(max(res, w*k))하면 추가 메모리 사용을 최소화(공간 복잡도 O(1))할 수 있어 대용량 데이터 처리 시 훨씬 효과적이라고 볼 수 있다.

    3. 굳이 리스트 두 번 안 훑고 루프 한 번에 끝내는 법을 익히는 게 효과적.
'''

#다시 짠 코드
import sys
input = sys.stdin.readline

###값 받기
N = int(input())
rope = []
for i in range(N):
    rope.append(int(input()))

###내림차순 정렬
rope.sort(reverse=True)

###가장 큰 값 계산, enumerate 사용
result = 0
for index, elem in enumerate(rope, 1):
    result = max(result, index*elem)
print(result)

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