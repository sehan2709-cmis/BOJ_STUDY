'''
1. lost와 reserve 교집합
    a. 확인
    b. answer에 값 더하기
    c. 두 리스트 모두에 제거

2. reserve 숫자 하나씩 보고 lost에 +-1이 있는지 확인.

기본 제공:
    def solution(n, lost, reserve):
    answer = 0
    return answer
'''


def solution(n, lost, reserve):
    answer = 0

    print("[before delete]")
    print("lost: ", lost)
    print("reserve: ", reserve)
    intersec = list(set(lost) & set(reserve)) #lost와 reserve 교집합 확인
    answer += len(intersec) #answer에 값 더하기
    print("intersec: ", intersec)
    
    #두 리스트 모두에 제거
    lost.remove(intersec)
    reserve.remove(intersec)

    print()
    print()
    print("[after delete]")
    print("lost: ", lost)
    print("reserve: ", reserve)
    
    print()


    return answer

    

''' 
1차 코드:
    메모리:  KB
    시간:  ms
    코드 길이:  B

2차 코드:
    메모리:  KB
    시간:  ms
    코드 길이:  B
'''

'''
[문제: 체육복 (그리디 알고리듬)]
Level: 1
기출: 백준 https://www.acmicpc.net/problem/1052

문제:
    점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다.
    학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다.
    예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다.
    체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

    전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost,
    여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
    체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항:
    - 전체 학생의 수는 2명 이상 30명 이하입니다.
    - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
    - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
    - 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며,
      남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.


입출력 예
    n	lost	reserve	    return
    5	[2, 4]	[1, 3, 5]	5
    5	[2, 4]	[3]	        4
    3	[3]	    [1]	        2
    

입출력 예 설명
    예제 #1
    1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

    예제 #2
    3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
'''


'''
[코드 풀이 과정]
    #내가 처음에 작성한 코드
    

    코드:
    
    ---
    #다른 사람 제출 답안 1
    #출처: 
    ###코드:
    ---
    #다른 사람 제출 답안 2
    #출처:
    ###코드:
        
    생각 정리:
    
    
    ---------
    #"내 코드 vs 다른 사람" 배울 점은?
'''

'''
[버려진 잘못된 접근의 코드들]

'''