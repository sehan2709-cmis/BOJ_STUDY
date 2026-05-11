'''
내 코드 피드백:
    1. 반복문 최적화: 
        - 인덱스가 필요 없다면 'for char in N:' 형식이 더 가독성이 좋을지도

    2. 예외 처리: 
        - 숫자가 포함되지 않은 입력이 들어올 경우를 대비해 'if num != 0:' 조건을 고려
    
    3. 내장 함수 활용:
        - x.isalpha(): 알파벳인지 확인
        - x.isdigit(): 숫자인지 확인 (isnumeric()보다 일반적으로 더 많이 쓰임)
    
    4. 리스트 정렬:
        - 새로운 리스트를 만들 필요가 없다면 words.sort()가 메모리 효율적
'''

# 1. 입력 받기
data = input()
result = []
value = 0
has_digit = False  # 숫자가 한 번이라도 나왔는지 체크 (0만 여러 개일 경우 대비)

# 2. 문자열을 순회하며 분리
for x in data:
    if x.isalpha():  # 알파벳인지 확인
        result.append(x)
    else:            # 숫자인 경우
        value += int(x)
        has_digit = True

# 3. 알파벳 오름차순 정렬
result.sort()  # 별도의 리스트를 생성하지 않고 원본 리스트를 직접 정렬 (메모리 효율)

# 4. 숫자가 하나라도 존재했다면 가장 뒤에 합계 추가
if has_digit:
    result.append(str(value))

# 5. 최종 결과 출력 (리스트를 문자열로 합치기)
print(''.join(result))

'''
접근 법
입력값 받기.
하나씩 환인하여 문자면 따로 보관 + 숫자면 더하기
문자 sort하고 숫자 다 더한거 합쳐서 출력

---------
다른 사람 답안 예시 01: 
    data = input()
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in data:
        # 알파벳인 경우 결과 리스트에 삽입
        if x.isalpha():
            result.append(x)
        # 숫자는 따로 더하기
        else:
            value += int(x)

    # 알파벳을 오름차순으로 정렬
    result.sort()

    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))

    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
    print(''.join(result))

다른 사람 답안 예시 02: 
    S = input()
    n = 0
    result = []

    for c in S:
        if c.isnumeric():
            n += int(c)
        else:
            result.append(c)

    result.sort()

    if len(result) != len(S):
        result.append(str(n))

    print("".join(result))
---------
내 코드 피드백:
    1. 반복문 최적화: 
        - 인덱스가 필요 없다면 'for char in N:' 형식이 더 가독성이 좋을지도

    2. 예외 처리: 
        - 숫자가 포함되지 않은 입력이 들어올 경우를 대비해 'if num != 0:' 조건을 고려
    
    3. 내장 함수 활용:
        - x.isalpha(): 알파벳인지 확인
        - x.isdigit(): 숫자인지 확인 (isnumeric()보다 일반적으로 더 많이 쓰임)
    
    4. 리스트 정렬:
        - 새로운 리스트를 만들 필요가 없다면 words.sort()가 메모리 효율적

---------
내 첫 코드:
    N = input()
    num = 0
    words = []
    for i in range(len(N)):
        if '9' >= N[i] >= '0':
            num += int(N[i])
        else:
            words.append(N[i])

    words = sorted(words) 
    result = "".join(words) + str(num)
    print(result) 
'''


'''
[문자열 재정렬]
난이도: 하
풀이 시간: 20분
시간 제한: 1초
메모리 제한: 128 MB
기출: Facebook 인터뷰

문제
    알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

입력 조건
    - 첫째 줄에 하나의 문자열 S가 주어집니다 ( 1 <= S의 길이 <= 10,000 )

출려 조건
   - 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

입출력 예시
    입력 예시 01:
        K1KA5CB7

    출력 예시 01:
        ABCKK13

    입력 예시 02:
        AJKDLSI412K4JSJ9D

    출력 예시 02:
        ADDIJJJKKLSS20
'''