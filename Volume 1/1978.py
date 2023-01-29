n = int(input())
numbers = map(int, input().split())
primeNum = 0

for num in numbers:
    check = 0
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                check = 1
                break
              
        if check == 0:
            primeNum += 1
          
print(primeNum)