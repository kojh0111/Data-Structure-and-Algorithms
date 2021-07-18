"""
- 나는야 포켓몬 마스터 이다솜
Dictionary를 2개를 만드는게 더 효율적인 것 같습니다.
"""
import sys

input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
pokedex = {}
pokedexR = {}

for i in range(1, n + 1):
    pokemon = input().rstrip()  # rstrip은 input을 sys.stdin.readline로 할때 필요!
    pokedex[i] = pokemon
    pokedexR[pokemon] = i

for _ in range(m):
    question = input().rstrip()
    try:
        question = int(question)
        print(pokedex[question])
    except ValueError:
        print(pokedexR[question])


""" 시간초과
n, m = [int(x) for x in input().split()]

pokemons = []
for _ in range(n):
    pokemon = input()
    pokemons.append(pokemon)

for _ in range(m):
    question = input()
    try:
        question = int(question)
        print(pokemons[question - 1])
    except ValueError:
        print(pokemons.index(question) + 1)
"""
