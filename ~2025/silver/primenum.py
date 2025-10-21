#브루트포스 알고리즘 입문 문제
#https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations #소수 판별을 위한 함수


def solution(answers):
    result = set()
    for i in range(len(answers)):
        result |= set(map(int, map("".join, permutations(list(answers), i + 1)))) #순열을 이용해 모든 조합 생성
        # |= 는 합집합을 구하는 연산자
        # permutations: 순열을 구하는 함수
        # set: 중복 제거를 위한 집합 자료형
    
    result -= set([0, 1]) #0과 1은 소수가 아니므로 제거

    for i in range(2, int(max(result)**0.5) + 1): #에라토스테네스의 체 알고리즘
        #0.5 제곱근까지만 검사
        result -= set(range(i*2, max(result)+1, i)) #i의 배수들을 제거

    return len(result) #남은 수의 개수가 소수의 개수

'''
### 배운 점
- [|= 연산자](https://velog.io/@nayoon-kim/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%97%B0%EC%82%B0%EC%9E%90)    
- [permutations() 기능](https://pearlluck.tistory.com/468)
- set() 집합 자료형
- 소수 찾는 다양한 방식
    - 제곱근까지만 검사
    - 에라토스테네스의의 체
'''

'''
프로그래머스 소수 찾기 (백준 기준 실3~1 예상)


기본 제공 코드
    def solution(answers):
        answer = []
        return answer

문제
    한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
    각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

    
제한 조건
    numbers는 길이 1 이상 7 이하인 문자열입니다.
    numbers는 0~9까지 숫자만으로 이루어져 있습니다.
    "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

입출력 예
    numbers	return
    "17"	3
    "011"	2

입출력 예 설명
    예제 #1
        [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

    예제 #2
        [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.
        (11과 011은 같은 숫자로 취급합니다.)
'''