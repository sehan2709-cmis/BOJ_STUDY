#풀이과정
#26 length를 가진 배열 array만듬. (모두 -1)
#단어 S를 입력 받음.
#S의 첫번쨰 알파벳 부터 시작하여 array에 순서 값을 늠 (배열의 값이 -1일떄만)

'''
방법 1:
array = [-1]*26
S = input()

for i in range(len(S)):
    if(array[ord(S[i])-97] == -1):
        array[ord(S[i])-97] = i

print(*array, sep=" ")


방법 2:
'''

S = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha:
    if i in S:
        print(S.index(i), end = " ")
    else:
        print(-1, end = " ")
