import re
#input = open('input.txt','r').readline #개인 확인용

def makeTable(pattern):
    l = len(pattern)
    table= [0]*l
    j = 0

    for i in range(1, l):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return(table)

def kmpSearch(text, pattern):
    table = makeTable(pattern)
    result = []

    n, m = len(text), len(pattern)
    i, j = (0, 0)

    while(i < n):
        if(text[i] == pattern[j]):
            i += 1
            j += 1

            if(j == m):
                result.append(i - j)
                j = table[j - 1]
        else:
            if(j > 0):
                j = table[j - 1]
            else:
                i += 1

    return(result)


S = re.sub(r"[0-9]", "", input())
K = input()
result = kmpSearch(S, K)

print(1) if result else print(0)

'''
백준 16172번 찾기
KMP을 활용한 문자열 찾기
KMP알고리듬을 활용한 1305번은 플래1이면서 이거는 왜 브론즈인지 잘 모르겠지만 일단 복습겸 다시 한번 풀어보쟈.

입력:
    첫 번째 줄에는 알파벳 소문자, 대문자, 숫자로 이루어진 문자열 S가 주어진다. (1 ≤ |S| ≤ 200,000) 두 번째 줄에는 성민이가 찾고자 하는 알파벳 소문자, 대문자로만 이루어진 키워드 문자열 K가 주어진다. (1 ≤ |K| ≤ 200,000)
    단, 입력으로 들어오는 키워드 문자열 K의 길이는, 교과서의 문자열 S보다 짧거나 같다.

출력:
    첫 번째 줄에 성민이가 찾고자 하는 키워드가 교과서 내에 존재하면 1, 존재하지 않으면 0을 출력한다.

백준 예시 1
    예시 입력값 1: 
    1q2w3e4r5t6y
    qwerty

    예시 출력값 1:
    1

백준 예시 2
    예시 입력값 2: 
    1ovey0uS2
    veS

    예시 출력값 2:
    0
'''