#브루트포스, 문자열, 정렬 문제

string = input()

# 사전순으로 가장 큰 수를 미리 입력
answer = "z" * len(string)

# 세 단어로 나누기 위해서 두 번을 자름
# 시간 복잡도: O(n^2)
for i in range(1, len(string) - 1):
    for j in range(i + 1, len(string)):
        s1 = string[:i][::-1]
        s2 = string[i:j][::-1]
        s3 = string[j:][::-1]
        new_string = s1 + s2 + s3
        answer = min(answer, new_string)  # 사전순으로 더 앞선 수를 가져옴

print(answer)

###wrong for some reason. have to find out tomorrow.
# word = input()
# result = [''] * len(word)
# result_idx = 0

# move = [0,0,0]
# if(len(word) % 3 == 0):
#     move = [int(len(word)/3)] * 3
# else:
#     left = len(word) % 3
#     mark = int(len(word) / 3)
#     move = [mark + left, (mark + left)*2, (mark + left)*2 + left]

# for i in range(3):
#     if i == 0:
#         for j in range(move[i], 0, -1):
#             result[result_idx] = word[j-1]
#             result_idx += 1
#     else:
#         for j in reversed(range(move[i-1], move[i])):
#             result[result_idx] = word[j]
#             result_idx += 1

# print(''.join(result))

'''
백준 1251 단어 나누기 (실버 5)
시간 제한: 2초
메모리 제한: 128 MB

문제
    알파벳 소문자로 이루어진 단어를 가지고 아래와 같은 과정을 해 보려고 한다.
    먼저 단어에서 임의의 두 부분을 골라서 단어를 쪼갠다.
    즉, 주어진 단어를 세 개의 더 작은 단어로 나누는 것이다.
    각각은 적어도 길이가 1 이상인 단어여야 한다.
    이제 이렇게 나눈 세 개의 작은 단어들을 앞뒤를 뒤집고, 이를 다시 원래의 순서대로 합친다.

    예를 들어,
        단어 : arrested
        세 단어로 나누기 : ar / rest / ed
        각각 뒤집기 : ra / tser / de
        합치기 : ratserde

    단어가 주어지면, 이렇게 만들 수 있는 단어 중에서 사전순으로 가장 앞서는 단어를 출력하는 프로그램을 작성하시오.


입력
    첫째 줄에 영어 소문자로 된 단어가 주어진다. 길이는 3 이상 50 이하이다.

출력
    첫째 줄에 구하고자 하는 단어를 출력하면 된다.

예제 결과물:
    예제 입력 0:
        mobitel

    예제 출력 0:
        bometil

    예제 입력 1:
        arrested

    예제 출력 1:
        ratserde
'''