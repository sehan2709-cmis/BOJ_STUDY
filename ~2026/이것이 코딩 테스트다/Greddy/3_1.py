'''
거스름돈 (예제 3-1) 문제.

문제
    당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
    손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.


#내가 처음에 작성한 코드
        cost = int(input())
        coins = 0
        coin = {500, 100, 50, 10}

        while(1):
            if cost >= 500:
                coins += 1
                cost = cost - 500
            elif cost >= 100:
                coins += 1
                cost = cost - 100
            elif cost >= 50:
                coins += 1
                cost = cost - 50
            elif cost >= 10:
                coins += 1
                cost = cost - 10
            else:
                break

        print(coins, "개의 동전이 나감")
        a = 1260 // 500
        print("1260 // 500 = ", a)

#책의 답안 예시 3-1.py
        n = 1250
        count = 0

        #큰 단위의 화폐부터 차례대로 확인
        coin_types = [500, 100, 50, 10]

        for coint in coin_types:
            count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
            n %= coin
        print(count)

딱 봐도 예시 답안이 간결하고 깔끔하다.
파이썬 문법을 잘 몰라서 그런걸까? 아님 풀다보면 저런 코드도 짤 수 있는 걸까?
파이썬 문법과 꼼수(?)라고 말할 수 있는 트릭들을 배우는게 좋을 것 같기는 하다.

"예시 vs 내 코드" 배울 점
    for coin in coin_types
        리스트 안에 있는 숫자들을 하나씩 coin이라는 변수에 담아 반복.
        if-elif를 4번 쓸 필요 없이, 동전 종류가 100개로 늘어나도 리스트만 수정하면 됌. (확장성)

    // (몫 연산자)
        1260 // 500 = 2가 나옴
        500원짜리 2개라고 한 번에 결론을 낼 수 있음

    % (나머지 연산자)
        1260 % 500을 하면 260이 남음
        500원짜리로 계산 가능한 걸 모두 한 후 다음 단계에서 처리할 숙제만 남기는 깔끔한 방식
'''

#다시 짠 코드
cost = int(input("물건의 값: "))
paid = int(input("손님이 지불한 금액: "))
change = paid - cost

coins = [500, 100, 50, 10]
count = 0
for left in coins:
    count += change // left
    change = change % left

print("물건의 값: ", cost)
print("지불 금액: ", paid)
print("거스름 값: ", paid - cost)
print("거스름 동전 개수: ", count)