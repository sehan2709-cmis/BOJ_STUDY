n = int(input())
whole = []
half = 0

for i in range(n):
  place, population = map(int, input().split())
  whole.append((place, population))
  half += population

whole = sorted(whole, key=lambda x: x[0])

adding = 0
index = 0

while (1):
  adding += whole[index][1]
  if adding >= half/2:
    print(whole[index][0])
    break
  index += 1
