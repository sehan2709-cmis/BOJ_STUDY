'''
[첫 접근]
1. 테스트 케이스 T 받기
2. T 순서만큼 반복문 돌리기.
        P (진행할 함수 string으로 입력 받기)
        len(array)인 n 값 받기
        error = 0
        array 받기

        P len 만큼 반복문 (for i in P):
            if P == "R"
                배열 뒤집기 <- 이게 문제 였음. 플래그/불리안을 만들어서 뒤집는거를 매번하지 않도록 코드만 짜도 반복문 하나가 준다.
            elif P == "D"
                if n == 0:
                    error = 1
                    print("error")
                    break
                else:
                    array[0].remove()
        
        if(error=1):
            break
        else:
            print(array)
'''

T = int(input()) # 테스트 케이스 T 받기
for _ in range(T):
    p = input().strip() #p (진행할 함수 string으로 입력 받기)
    n = int(input().strip()) #len(array)인 n 값 
    

    raw_array = input().strip() # n이 0이어도 일단 읽어서 버퍼를 비워야 함
    data = []
    if n != 0:
        data = raw_array[1:-1].split(",")

    error = 0 #에러 확인 용
    reverse = 0

    for i in p:
        if i == "R": #R이면 뒤집기
            reverse = not(reverse)
        elif i == "D":
            if n > 0:
                if reverse:
                    del data[-1]
                else:
                    del data[0]
                
                n -= 1
            else: #n이 0이면 에러.
                error = 1
                print("error")
                break
    
    if error == 0:
        if reverse:
            data.reverse()
        print("[" + ",".join(data) + "]") #리스트의 숫자들을 문자열로 바꾼 뒤, 쉼표(,)를 기준으로 공백 없이 합침




# 2. T 순서만큼 반복문 돌리기.
#         P (진행할 함수 string으로 입력 받기)
#         len(array)인 n 값 받기
#         error = 0
#         array 받기

#         P len 만큼 반복문 (for i in P):
#             if P == "R"
#                 배열 뒤집기
#             elif P == "D"
#                 if n == 0:
#                     error = 1
#                     print("error")
#                     break
#                 else:
#                     array[0].remove()
        
#         if(error=1):
#             break
#         else:
#             print(array)

'''
[코드 풀이 과정]
    #[내가 처음에 작성한 코드]
        첫 접근은 가장 밑에 "잘못 된 접근으로 실패한 코드." 확인.
        -> 간단 요약하면 시간 초과함.
        너무 하나하나 그대로 코딩한듯 하다. 어떻게 최적화 해야 할까?

        30분 넘게 고민했지만 해결하지 못해서 [다른 사람 제출 답안 1]을 참고했다.
        블로그가 나와 매우 동일하게 접근했고. 동일하게 시간 초과로 실패했다고 한다.


    ---
    #[다른 사람 제출 답안 1]
        ##출처: https://hongcoding.tistory.com/44
        ##코드:
            import sys
            from collections import deque

            t = int(input())

            for i in range(t):
                p = sys.stdin.readline().rstrip()
                n = int(input())
                arr = sys.stdin.readline().rstrip()[1:-1].split(",")
                queue = deque(arr)

                rev, front, back = 0, 0, len(queue)-1
                flag = 0
                if n == 0:
                    queue = []
                    front = 0
                    back = 0

                for j in p:
                    if j == 'R':
                        rev += 1
                    elif j == 'D':
                        if len(queue) < 1:
                            flag = 1
                            print("error")
                            break
                        else:
                            if rev % 2 == 0:
                                queue.popleft()
                            else:
                                queue.pop()
                if flag == 0:
                    if rev % 2 == 0:
                        print("[" + ",".join(queue) + "]")
                    else:
                        queue.reverse()
                        print("[" + ",".join(queue) + "]")

        ##생각 정리:
            블로그를 작성한 사람은 reverse에 시간이 많이 소요 되는 것을 확인하고
            뒤집는 횟수를 저장하여 왼족 오른쪽을 지울지 확인 함. + 마지막에 짝수면 안뒤짐음. 홀수면 마지막에 한번 뒤집는다.
    ---
    #[다른 사람 제출 답안 2]
        ##출처: https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-5430%EB%B2%88-AC-python-%EB%8B%A8%EC%88%9C-%EA%B5%AC%ED%98%84
        ##코드:
            import sys
            from collections import deque

            input = sys.stdin.readline

            t = int(input())


            answer = []
            for _ in range(t):
                p = input().strip()
                n = int(input().strip())
                arr = list(input().strip()[1:-1].split(","))
                q = deque(arr)
                reverse = 0
                error = 0
                if n == 0:
                    q = []

                for i in p:
                    if i == "R":
                        reverse = not reverse
                    else:
                        if len(q) < 1:
                            answer.append("error")
                            error = 1
                            break
                        else:
                            if reverse:
                                q.pop()
                            else:
                                q.popleft()

                if not error:
                    if reverse:
                        q.reverse()
                    answer.append("[" + ",".join(q) + "]")

            for a in answer:
                print(a)
    

        ##생각 정리:
            여기 블로그도 동일하게 R를 확인한 것을 볼 수 있다.
            다만 여기는 첫 블로그보다 영리하게 숫자를 세는 것이 아닌 bool로 확인하여 스위치처럼 활용.
    
    -----------
    #["내 코드 vs 다른 사람" 배울 점은?]
        시간을 줄일 수 있는 법이 뭔지를 좀더 고민해보쟈.
        reverse와 같은 python의 좋은 기능들도 있지만.
        그 기능안에 시간 복잡도또한 포함된다는 것을 기억하고 부담이 되지 않을때 활용하자.
'''


'''
AC (백준 5430)
난이도: 골드5
시간 제한: 1초
메모리 제한: 256MB 
기출: 백준 https://www.acmicpc.net/problem/5430

문제:
    선영이는 주말에 할 일이 없어서 새로운 언어 AC를 만들었다. AC는 정수 배열에 연산을 하기 위해 만든 언어이다. 이 언어에는 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.
    함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
    함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.
    배열의 초기값과 수행할 함수가 주어졌을 때, 최종 결과를 구하는 프로그램을 작성하시오.

입력 조건:
    첫째 줄에 테스트 케이스의 개수 T가 주어진다. T는 최대 100이다.
    각 테스트 케이스의 첫째 줄에는 수행할 함수 p가 주어진다. p의 길이는 1보다 크거나 같고, 100,000보다 작거나 같다.
    다음 줄에는 배열에 들어있는 수의 개수 n이 주어진다. (0 ≤ n ≤ 100,000)
    다음 줄에는 [x1,...,xn]과 같은 형태로 배열에 들어있는 정수가 주어진다. (1 ≤ xi ≤ 100)
    전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않는다.

출력 조건:
    각 테스트 케이스에 대해서, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력한다. 만약, 에러가 발생한 경우에는 error를 출력한다.

입력 예시 1:
    4
    RDD
    4
    [1,2,3,4]
    DD
    1
    [42]
    RRD
    6
    [1,1,2,3,5,8]
    D
    0
[]

출력 예시 1:
    [2,1]
    error
    [1,2,3,5,8]
    error
'''

'''
잘못 된 접근으로 실패한 코드.
    [첫 접근 -> 시간 초과. 뒤집는 것이 시간을 다소 많이 소모 하는 것 같다.]
    1. 테스트 케이스 T 받기
    2. T 순서만큼 반복문 돌리기.
            P (진행할 함수 string으로 입력 받기)
            len(array)인 n 값 받기
            error = 0
            array 받기

            P len 만큼 반복문 (for i in P):
                if P == "R"
                    배열 뒤집기
                elif P == "D"
                    if n == 0:
                        error = 1
                        print("error")
                        break
                    else:
                        array[0].remove()
            
            if(error=1):
                break
            else:
                print(array)

    코드:
        T = int(input()) # 테스트 케이스 T 받기
        for _ in range(T):
            p = input() #p (진행할 함수 string으로 입력 받기)
            n = int(input()) #len(array)인 n 값 
            
            # 수정된 입력부
            raw_array = input().strip() # n이 0이어도 일단 읽어서 버퍼를 비워야 함

            data = []
            if n != 0:
                data = raw_array[1:-1].split(",")

            error = 0 #에러 확인 용

            for i in p:
                if i == "R": #R이면 뒤집기
                    data.reverse() 
                elif i == "D":
                    if n > 0:
                        del data[0]
                        n -= 1
                    else: #n이 0이면 에러.
                        error = 1
                        print("error")
                        break
            
            if error == 0:
                print("[" + ",".join(data) + "]") #리스트의 숫자들을 문자열로 바꾼 뒤, 쉼표(,)를 기준으로 공백 없이 합침
'''