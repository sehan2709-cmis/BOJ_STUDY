def sort_key(x):
  return x[0]


n = int(input())
X = []
A = []
half = 0

for i in range(n):
  userInput = list(map(int, input().split()))
  X.append(userInput[0])
  A.append(userInput[1])
  half += userInput[1]

whole = list(zip(X, A))
whole = sorted(whole, key=sort_key)

half = half / 2
closest = 1000000001
index = 0

while (1):
  add = sum(whole[:index])
  if (abs(half - add) < closest):
    closest = abs(half - add)
  else:
    print(index - 1)
    break
  index += 1
