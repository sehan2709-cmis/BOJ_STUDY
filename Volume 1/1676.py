from math import factorial

input = int(input())
result = 0

for i in str( factorial(input))[::-1]:
    if i != '0':
        break
    result += 1
  
print(result)