'''
1. 전처리: 여벌이 있는데 도난당한 학생은 두 명단에서 모두 뺀다 (set 차집합).
2. 대여: 빌려야 할 학생을 정렬한 뒤, 앞 번호 → 뒷 번호 순으로 여벌이 있는지 확인한다.
3. 반환: 전체 인원에서 끝까지 못 빌린 학생만 뺀다.

기본 제공:
    def solution(n, lost, reserve):
    answer = 0
    return answer
'''

def solution(n, lost, reserve):
    # 1. 집합으로 변환하여 여벌 소유자의 도난 케이스 즉시 제거
    actual_lost = set(lost) - set(reserve)
    actual_reserve = set(reserve) - set(lost)

    # 2. 정렬된 '진짜 도난 학생' 명단을 순회하며 빌려주기 시도
    for l in sorted(actual_lost):
        if l - 1 in actual_reserve: #i-1
            actual_reserve.remove(l - 1)
        elif l + 1 in actual_reserve: #i+1
            actual_reserve.remove(l + 1)
        else:  # 못 빌림
            n -= 1
            
    return n

lost_list = [2, 4]
reserve_list = [3]
a = 5
print(solution(a, lost_list, reserve_list))

'''
첫 코드 실행결과:
    테스트 1 〉	통과 (0.01ms, 9.23MB)
    테스트 2 〉	통과 (0.01ms, 9.24MB)
    테스트 3 〉	통과 (0.01ms, 9.1MB)
    테스트 4 〉	통과 (0.01ms, 9.23MB)
    테스트 5 〉	통과 (0.01ms, 8.99MB)
    테스트 6 〉	통과 (0.01ms, 9.29MB)
    테스트 7 〉	통과 (0.01ms, 9.09MB)
    테스트 8 〉	통과 (0.01ms, 9.24MB)
    테스트 9 〉	통과 (0.01ms, 9.24MB)
    테스트 10 〉	통과 (0.01ms, 9.32MB)
    테스트 11 〉	통과 (0.01ms, 9.04MB)
    테스트 12 〉	통과 (0.01ms, 9.2MB)
    테스트 13 〉	통과 (0.01ms, 9.21MB)
    테스트 14 〉	통과 (0.01ms, 9.07MB)
    테스트 15 〉	통과 (0.01ms, 9.09MB)
    테스트 16 〉	통과 (0.01ms, 9.22MB)
    테스트 17 〉	통과 (0.01ms, 9.24MB)
    테스트 18 〉	통과 (0.01ms, 9.07MB)
    테스트 19 〉	통과 (0.01ms, 9MB)
    테스트 20 〉	통과 (0.01ms, 9.22MB)
    테스트 21 〉	통과 (0.01ms, 9.25MB)
    테스트 22 〉	통과 (0.01ms, 9.11MB)
    테스트 23 〉	통과 (0.01ms, 9.27MB)
    테스트 24 〉	통과 (0.01ms, 9.23MB)
    테스트 25 〉	통과 (0.01ms, 9.17MB)
    테스트 26 〉	통과 (0.01ms, 9.17MB)
    테스트 27 〉	통과 (0.01ms, 9.23MB)
    테스트 28 〉	통과 (0.01ms, 9.33MB)
    테스트 29 〉	통과 (0.01ms, 9.03MB)
    테스트 30 〉	통과 (0.01ms, 9.2MB)

두 번째 코드 실행결화:
    테스트 1 〉	통과 (0.01ms, 9.27MB)
    테스트 2 〉	통과 (0.01ms, 9.15MB)
    테스트 3 〉	통과 (0.01ms, 9.08MB)
    테스트 4 〉	통과 (0.01ms, 9.15MB)
    테스트 5 〉	통과 (0.01ms, 9.22MB)
    테스트 6 〉	통과 (0.01ms, 9.09MB)
    테스트 7 〉	통과 (0.01ms, 9.15MB)
    테스트 8 〉	통과 (0.01ms, 9.21MB)
    테스트 9 〉	통과 (0.01ms, 9.18MB)
    테스트 10 〉	통과 (0.01ms, 9.22MB)
    테스트 11 〉	통과 (0.01ms, 9.11MB)
    테스트 12 〉	통과 (0.01ms, 9.19MB)
    테스트 13 〉	통과 (0.01ms, 9.11MB)
    테스트 14 〉	통과 (0.01ms, 9.29MB)
    테스트 15 〉	통과 (0.01ms, 9.24MB)
    테스트 16 〉	통과 (0.01ms, 9.23MB)
    테스트 17 〉	통과 (0.01ms, 9.18MB)
    테스트 18 〉	통과 (0.01ms, 9.29MB)
    테스트 19 〉	통과 (0.01ms, 9.15MB)
    테스트 20 〉	통과 (0.01ms, 9.23MB)
    테스트 21 〉	통과 (0.01ms, 9.11MB)
    테스트 22 〉	통과 (0.01ms, 9.17MB)
    테스트 23 〉	통과 (0.01ms, 9.2MB)
    테스트 24 〉	통과 (0.01ms, 9.21MB)
    테스트 25 〉	통과 (0.01ms, 9.26MB)
    테스트 26 〉	통과 (0.01ms, 9.21MB)
    테스트 27 〉	통과 (0.01ms, 9.16MB)
    테스트 28 〉	통과 (0.01ms, 9.11MB)
    테스트 29 〉	통과 (0.01ms, 9.21MB)
    테스트 30 〉	통과 (0.01ms, 9.21MB)
'''

'''
[문제: 체육복 (그리디 알고리듬)]
Level: 1
기출: 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/42862?gad_source=1&gad_campaignid=23716289893&gbraid=0AAAAAC_c4nAELB0hq19Vu-vp-2APd1SKH&gclid=CjwKCAjw7vzOBhBxEiwAc7WNrxEWoQmZMFU67T5sn6d3KoPLAqttA19EulZAYKgruBH_7LAWn0IMWBoCG94QAvD_BwE

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
        1. 리스트 정렬 및 교집합(중복) 제거
            - lost와 reserve 리스트 정렬
            - 두 리스트의 교집합(빌려줄 수 없는 여벌 소유자) 확인
            - 확인된 인원을 두 리스트에서 모두 제거

        2. 여벌 옷 대여 로직
            - reserve 숫자를 하나씩 확인
            - i-1(앞번호) 학생이 lost에 있으면 제거
            - 앞번호가 없을 경우, i+1(뒷번호) 학생이 lost에 있는지 확인 후 제거

        3. 최종 인원 계산
            - 전체 학생 수(n)에서 끝까지 남은 lost 인원 제외
            - 결과값 리턴

    내 첫 코드:
        def solution(n, lost, reserve):
            lost.sort()
            reserve.sort()
            
            #두 리스트 모두에 제거
            intersec = list(set(lost) & set(reserve)) #lost와 reserve 교집합 확인
            for i in intersec:
                lost.remove(i)
                reserve.remove(i)

            #2. reserve 숫자 하나씩 보고 lost에 +-1이 있는지 확인.
            for i in reserve:
                if i-1 in lost: # reserve[i]-1
                    lost.remove(i-1)
                elif i+1 in lost: # reserve[i]+1
                    lost.remove(i+1)

            #값 리턴
            return(n - len(lost))
    
    ---
    #다른 사람 제출 답안 1
        ##출처: https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
        ##코드:
            def solution(n, lost, reserve):
                # 정렬
                lost.sort()
                reserve.sort()
                
                # lost, reserve에 공통으로 있는 요소 제거
                for i in reserve[:]:
                    if i in lost:
                        reserve.remove(i)
                        lost.remove(i)
                
                # 체육복 빌려주기(나의 앞 번호부터 확인)
                for i in reserve:
                    if i-1 in lost:
                        lost.remove(i-1)
                    elif i+1 in lost:
                        lost.remove(i+1)
                
                return n-len(lost)

        ##생각 정리:
            1. 교집합 제거 방식
                내 코드:
                    - 집합 연산(&)을 사용하여 중복 요소를 찾는 과정이 매우 직관적이고 빠릅니다.
                    - 별도의 메모리 공간(intersec 리스트)을 만들어 중복 요소를 저장한 뒤, 원본 리스트에서 하나씩 지워나갑니다.
                
                슬라이싱 복사본([:]) 방법:
                    - 차이점: reserve[:]는 리스트의 전체 복사본을 생성한다.
                    - 이유: 파이썬에서 리스트를 순회(for)하면서 동시에 요소를 삭제(remove)하면,
                           인덱스가 뒤로 밀려 요소를 건너뛰는 버그가 발생할 수 있습니다.
                           
                           이를 방지하기 위해 "복사본을 돌면서 원본을 수정"한 것으로 보임.
                
                -> 상대 코드는 내 코드처럼 set으로 변환하는 과정 없이도 리스트 내부에서 즉시 처리할 수 있음
                -> 상대 코드가 좀더 직관적으로 논리가 가동석이 좋아 보임
    
    ---
    #다른 사람 제출 답안 2
        ##출처: https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B2%B4%EC%9C%A1%EB%B3%B5
        ##코드:
            def solution(n, lost, reserve):
                new_lost = set(lost) - set(reserve)
                new_reserve = set(reserve) - set(lost)
                for i in new_lost:
                    if i + 1 in new_reserve:
                        new_reserve.remove(i + 1)
                    elif i - 1 in new_reserve:
                        new_reserve.remove(i - 1)
                    else:
                        n-=1
                return n

        ##생각 정리:
            내 코드:
                - 리스트(List) 중심의 직관적 접근교집합 처리: set으로 교집합을 구한 뒤 다시 list로 변환하여 원본에서 remove()를 호출
                - 탐색 방식: reserve(빌려줄 사람)를 기준으로 루프를 돌며 lost(빌릴 사람)를 찾는다
                - 특징: 과정이 단계별로 명확할 순 있지만, list.remove()는 호출될 때마다 리스트를 처음부터 끝까지 훑어야 하므로
                       데이터가 많아질수록 속도가 느려질 수 있다 (O(N) 연산의 반복)
            
            다른 사람 코드:
                - 집합(Set) 중심의 효율적 접근교집합 처리: 차집합 연산(-)을 통해 시작부터 중복 요소를 제거한 새로운 집합(new_lost, new_reserve)을 만든다.
                - 탐색 방식: lost(빌려야 하는 사람)를 기준으로 루프를 돌며 여벌이 있는지 확인한다.
                - 특징: set 자료형을 적극 활용했음.
                       set에서 요소를 찾거나(in) 삭제하는 연산은 평균적으로 O(1) (상수 시간)에 수행되므로 성능 면에서 더 유리.

            -> 추가적으로 교집합을 매우 똑똑하게 처리함. set(lost) - set(reserve)

            상대 코드를 보며 들었던 궁금증?:
                3. 주의할 점 (버그 가능성)
                    그 번호 i+-1 확인할때 왜 +1을 먼저 확인하는지 이해가 잘 안됌.
                    new_lost가 정렬되지 않은 상태에서 +1부터 확인하면, 최적의 해를 구하지 못하는 케이스가 생길 수 있지 않을까?
                    (예: 2번이 빌려야 하고 1, 3번이 여벌이 있을 때, 뒤 번호부터 빌려버리면 다른 사람이 못 빌리는 상황 발생)

                    따라서 set을 쓰더라도 순회가 필요할 때는 sorted(new_lost)와 같이 정렬된 순서로 접근하는 것이 훨씬 안전할 수도 있지 않을까 싶다.
'''

'''
[버려진 잘못된 접근의 코드들]
'''