'''
큰 수의 법칙
난이도: 하
풀이 시간: 30분
시간 제한: 1초
메모리 제한: 128MB
기출: 2019 국가 교육기관 코딩 테스트

문제
    '큰 수의 법칙'은 일반적으로 통계 분야에서 다루어지는 내용이지만 동빈이는 본인만의 방식으로 다르게 사용하고 있다.
    동빈이의 큰 수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
    단, 배열의 특정한 인덱스 (번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
    
    예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때 M이 8번이고, K가 3이라고 가정하자.
    이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는
    6+6+6+5+6+6+6+5인 46이 된다.

    단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다. 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을때
    M이 7이고, K가 2라고 가정하자. 이경우 두번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다.
    결과적으로 4+4+4+4+4+4+4인 28이 도출된다.

    배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 동빈이의 큰 수의 법칙에 따른 결과를 출력하시오.

    입력 조건:
    - 첫째 줄에 N(2 <= N <= 1,000),
              M(1 <= M <= 10,000),
              K(1 <= K <= 10,000)의
       자연수가 주어지며, 각 자연수는 공백으로 구분한다.
    
    - 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000이하의 수로 주어진다.
    - 입력으로 주어지는 K는 항상 M보다 작거나 같다.

    출력 조건:
    - 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

    입력 예시:
    5 8 3
    2 4 5 4 6

    출력 예시:
    46

#내가 처음에 작성한 코드
        N, M, K = map(int, input().split())
        numbers = list(map(int, input().split()))

        #two biggest number.
        numbers.sort(reverse=True)

        n = M/(K+1) #두번째 숫자가 반복되는 횟수
        result =  (numbers[0] * n * K) + (numbers[0] * (M%(K+1))) + (numbers[1]*(n))

        print(int(result))

#책의 답안 예시
        # N, M, K를 공백으로 구분하여 입력받기
        N, M, K = map(int, input().split())
        # N개의 수를 공백으로 구분하여 입력받기
        numbers = list(map(int, input().split()))

        data.sort() #입력받은 수를 정렬하기
        first = data[n-1] #첫 번째로 큰 수
        second = data[n-2] #두 번째로 큰 수

        result = 0
        while True:
            for i in range(k): #가장 큰 수를 K번 더하기
                if m == 0: #m이 0이라면 반복문 탈출
                    break
                result += first
                m -= 1 #더할 때 마다 1씩 빼기
            if m == 0 #m이 0이라면 반복문 탈출
                break
            result += second #두 번째로 큰 수를 한번 더하기
            m -= 1 #더할 때마다 1씩 빼기

        print(result) #최종 답안 출력

#책의 답안 예시 2
        # N, M, K를 공백으로 구분하여 입력받기
        N, M, K = map(int, input().split())
        # N개의 수를 공백으로 구분하여 입력받기
        numbers = list(map(int, input().split()))

        data.sort() #입력받은 수를 정렬하기
        first = data[n-1] #첫 번째로 큰 수
        second = data[n-2] #두 번째로 큰 수

        # 가장 큰 수가 더해지는 횟수 계산
        count = int(m / (k + 1)) * k
        count += m % (k + 1)

        result = 0
        result += (count) * frist #가장 큰 수 더하기
        result += (m - count) * second #두 번째로 큰 수 더하기

        print(result) #최종 답안 출력



#"예시 vs 내 코드" 배울 점
        노가다보다 본능적으로 수식 찾은 나 칭찬해 ㅎㅎ
        근데 왜 M/(K+1)만 생각하고 한번에 할 생각을 못 했을 까 ㅋㅋ
        1은 되고 2는 안돼나 보다.
        좀더 깊게 생각해자!
'''

#다시 짠 코드
N, M, K = map(int, input().split())
numbers = list(map(int, input().split()))

#two biggest number.
numbers.sort(reverse=True)

n = int((M / (K+1)) * K + (M % (K+1))) #첫번째 순서가 반복되는 횟수
result =  (numbers[0] * n) + (numbers[1] * (M - n))

print(result)