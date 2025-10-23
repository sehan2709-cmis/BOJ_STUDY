#수학, 사칙연산
#https://www.acmicpc.net/problem/32326

R = int(input())
G = int(input())
B = int(input())
cost = R * 3 + G * 4 + B * 5
print(cost)

'''
백준 32326번 Conveyor Belt Sushi (브5)


기본 제공 코드
    def solution(answers):
        answer = []
        return answer

문제
    There is a new conveyor belt sushi restaurant in town.
    Plates of sushi travel around the restaurant on a raised conveyor belt and customers choose what to eat by removing plates.

    Each red plate of sushi costs $3, each green plate of sushi costs $4, and each blue plate of sushi costs $5.

    Your job is to determine the cost of a meal, given the number of plates of each colour chosen by a customer.

    
입력
    The first line of input contains a non-negative integer, R, representing the number of red plates chosen. The second line contains a non-negative integer, G, representing the number of green plates chosen. The third line contains a non-negative integer, B, representing the number of blue plates chosen.

출력
    Output the non-negative integer, C, which is the cost of the meal in dollars.

입출력 예
    예제 입력 0:
        0
        2
        4
    
    예체 출력 0:
        28
'''