import sys
input = sys.stdin.readline

numbers, inputs = map(int, input().split())

pokemons = {}
for i in range(numbers):
    inp = input().rstrip()
    pokemons[i+1] = inp
    pokemons[inp] = i+1
    
for i in range(inputs):
    inp = input().rstrip()
    if inp.isdigit():
        print(pokemons[int(inp)])
    else:
        print(pokemons[inp])