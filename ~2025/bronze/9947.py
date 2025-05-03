#input = open('input.txt','r').readline #개인 확인용

while True:
    a, b = input().split()
    if a == "#" and b == "#":
        break

    n = int(input())
    a_score = 0
    b_score = 0

    for _ in range(n):
        call, result = input().split()
        if call == result:
            a_score += 1
        else:
            b_score += 1

    print(f"{a} {a_score} {b} {b_score}")


'''
백준 9947번 Coin tossing
간단한imple 반복문+조건문 문제

문제
When I was at school, many, many years ago, we used to play a simple game involving tossing a coin. The first player would call "heads" or "tails", the second would toss the coin. The first player gained a point for every correct call, the second player gained one for every incorrect call. When we got bored, we added up the scores!

입력
    Input for this problem will consist of a number of games. Each game will begin with a line containing 2 names of no more than 20 letters each and separated by a space. The second line of each game will contain a single positive integer, n, specifying the number of recorded coin tosses (0 < n <= 1000). n coin tosses follow, each on a single lines containing 2 characters (either 'H' or 'T' – "heads" or "tails"), separated by a space. The first character denotes the call and the second denotes the result. Input will be terminated by a line containing just # #.

출력
    Output will be one line for each game. The line will give the name of the first player (as recorded in the input), followed by the first player's score, followed by the name of the second player, followed by the second player's score. Entries on a line will be separated by a single space.

백준 예시: 
예제 입력 1:
    Sally John
    5
    H H
    H T
    H H
    T T
    T H
    Eloise Ahmed
    4
    H T
    T T
    H H
    T H
    # #

예제 출력 1:
    Sally 3 John 2
    Eloise 2 Ahmed 2
'''