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
                result.append(i - j + 1) #문제에서 1을 안더하면 안됌. 왜지;
                j = table[j - 1]
        else:
            if(j > 0):
                j = table[j - 1]
            else:
                i += 1

    return(result)


T = input()
P = input()
result = kmpSearch(T, P)

print(len(result))
if result: #result가 비어있으면 출력을 하지 않음
    print(*result)

'''
 백준 1786번 찾기
 KMP을 활용한 문자열 찾기
 ctrl+f 구현하기
 

백준 예시: 
ABC ABCDAB ABCDABCDABDE
ABCDABD
'''