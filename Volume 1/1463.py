x = int(input())
dp = [0]*(x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
      
print(dp[x])

#처음에 문제를 풀때 if(%2) elif(%3) else(--) 라고 생각했지만
#위와 같이 풀었을때
#10의 경우에 
#10 -> 5 -> 4 -> 2 -> 1로 4번안에 만들어 진다.

#하지만 문제는 연산을 사용하는 횟수의 "최솟값"을 원하기에 아래와 같이
#10 -> 9 -> 3 -> 1 로 3번 만에 만들어야 한다.

#그리하여 dp리스트를 만들어 
#각 dp의 index가 1이 되기 필요한 최솟값을 저장케 하여 index가 x의 길이가 될 때까지 구해 나아가는 방식으로 문제를 해결하였다.

# min(dp[i], dp[i//2] + 1) 와 min(dp[i], dp[i//3] + 1) 는 7,9 줄 코드는
# index가 2 혹은 3으로 나누어 떨어질 때, 둘 중 최솟값을 dp[i]에 저장하게 하였다.