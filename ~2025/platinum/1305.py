#input = open('input.txt','r').readline #개인 확인용

def makeTable(pattern):
    l = len(pattern)
    table= [0]*l
    prefix_len = 0

    for i in range(1, l):
        while prefix_len > 0 and pattern[i] != pattern[prefix_len]:
            prefix_len = table[prefix_len-1]
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            table[i] = prefix_len

    return(prefix_len)

L = int(input())
text = input()
result = makeTable(text)

print(L-result)

'''
백준 1305번 광고
KMP을 활용한 문자열 찾기
 
제한:
1 ≤ L ≤ 1,000,000
광고판에 보이는 문자열은 알파벳 소문자로만 이루어져 있다.

백준 예시: 
5
aaaaa
'''