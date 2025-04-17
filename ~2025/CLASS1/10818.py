num = int(input())
array = list(map(int, input().split()))
array.sort()

print(array[0], array[num-1])