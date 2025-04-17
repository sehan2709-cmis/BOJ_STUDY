n = int(input())
man = sorted(list(map(int, input().split())))
woman = sorted(list(map(int, input().split())))

count = 0
index1 = 0
index2 = 0
mode = 0

while (1):
  if count >= n or index1 >= n or index2 >= n:
    print(count)
    break
  if mode == 0:
    if man[index1] > 0 or woman[-1 - index2] < 0:
      mode = 1
      index1 = 0
      index2 = 0
    elif abs(man[index1]) > abs(woman[-1 - index2]):
      index1 += 1
      index2 += 1
      count += 1
    else:
      index2 += 1
  else:
    if man[-1 - index1] < 0 or woman[index2] > 0:
      print(count)
      break
    elif abs(man[-1 - index1]) < abs(woman[index2]):
      index1 += 1
      index2 += 1
      count += 1
    else:
      index1 += 1
