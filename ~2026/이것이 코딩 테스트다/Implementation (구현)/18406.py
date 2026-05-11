N = input()
half = len(N) // 2  # 정수 나눗셈 사용

left = sum(map(int, N[:half]))   # 0은 생략 가능
right = sum(map(int, N[half:]))  # 마지막 인덱스 생략 가능

if left == right:
    print("LUCKY")
else:
    print("READY")

'''
1. 입력 값을 받는다.
2. 무조건 짝수니 length/2 전까지 더하고 이후랑 비교
   (스트링으로 해서 그냥 인티져로 바꿔서 더한다)
3. 같으면 LUCKY 아니면 READY

---------
다른 사람 답안 예시01: 
    x = input()
    half = len(x)//2
    left = 0
    right = 0
    for i in range(0, half):
        left += int(x[i])
    for i in range(half, len(x)):
        right += int(x[i])
    if left == right:
        print("LUCKY")
    else:
        print("READY")

출처: https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-18406%EB%B2%88-%EB%9F%AD%ED%82%A4-%EC%8A%A4%ED%8A%B8%EB%A0%88%EC%9D%B4%ED%8A%B8-%ED%8C%8C%EC%9D%B4%EC%8D%AC

다른 사람 답안 예시02:
    arr = list(map(int, input()))
    print("LUCKY") if sum(arr[:len(arr) // 2]) == sum(arr[len(arr) // 2:]) else print("READY")

출처: https://yjg-lab.tistory.com/356
---------
내 코드 피드백:
    1. 정수 나눗셈 연산자 (//) 사용: 
        코드가 간결해지고, 실수(float) 연산 과정을 거치지 않아 의도가 명확해집니다.
    2. 슬라이싱(Slicing)의 생략 문법 활용
        불필요한 함수 호출(len)과 숫자를 줄여 가독성을 높입니다.

---------
내 첫 코드:
    N = input()

    length = len(N)
    left = sum(map(int, N[0:int(length/2)]))
    right = sum(map(int, N[int(length/2):length]))

    if left == right:
        print("LUCKY")
    else:
        print("READY")
'''


'''
[18406 렄키 스트레이트]
난이도: 브2
풀이 시간: 20분
시간 제한: 1초
메모리 제한: 256 MB

문제
    어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
    특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하 여 럭키 스트레이트를 사용할 수 있다.
    현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 럭키 스트레이트를 사용할 수 있다면 " LUCKY "를, 사 용할 수 없다면 "READY "라는 단어를 출력한다. 또한 점수 NV의 자릿수는 항상 짝수 형태로만 주어진다. 예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않 는다.

입력 조건
    - 첫째 줄에 점수 이 정수로 주어진다. (10 ≤ N ≤ 99,999,999) 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

출려 조건
   - 첫째 줄에 럭키 스트레이트를 사용할 수 있다면 " LUCKY "를, 사용할 수 없다면 "READY "라는 단어를 출력한다.

입출력 예시
    입력 예시 01:
        123402

    출력 예시 01:
        LUCKY

    입력 예시 02:
        7755

    출력 예시 02:
        READY
'''