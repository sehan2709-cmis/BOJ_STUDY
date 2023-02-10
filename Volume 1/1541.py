formula = input().split('-')
nums = []

for i in formula:
  cnt = 0
  s = i.split('+')
  for j in s:
    cnt += int(j)
  nums.append(cnt)

result = nums[0]

for i in range(1, len(nums)):
  result -= nums[i]
print(result)