N, rol, col = map(int, input().split())
result = 0

while N != 0:
  N -= 1
  if rol < 2**N and col < 2**N:
    result += (2**N) * (2**N) * 0
  elif rol < 2**N and col >= 2**N:
    col -= (2**N)
    result += (2**N) * (2**N) * 1
  elif rol >= 2**N and col < 2**N:
    rol -= (2**N)
    result += (2**N) * (2**N) * 2
  else:
    rol -= (2**N)
    col -= (2**N)
    result += (2**N) * (2**N) * 3

print(result)