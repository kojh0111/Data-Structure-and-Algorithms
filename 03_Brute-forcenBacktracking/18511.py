"""
- 큰 수 구성하기
중복 순열을 활용한 문제풀이(Python의 itertools.product)
"""
from itertools import product
import sys

input = sys.stdin.readline
N, K = [int(x) for x in input().split()]
numlist = [x for x in input().split()]
comblist = [
    int("".join(x))
    for x in product(numlist, repeat=len(str(N)))  # 중복순열
    if int("".join(x)) <= N
]
if len(comblist) == 0:
    comblist = [
        int("".join(x)) for x in product([max(numlist)], repeat=len(str(N)) - 1)
    ]  # 자릿수가 하나 작아지면 가장 큰 수로만 구성된 숫자를 만들면 됨

print(max(comblist))  # 가장 큰 수 찾기
"""
from itertools import combinations_with_replacement
import sys

input = sys.stdin.readline
N, K = [int(x) for x in input().split()]
numlist = [x for x in input().split()]
comblist = [
    int("".join(x))
    for x in combinations_with_replacement(numlist, len(str(N)))
    if int("".join(x)) <= N
]
if len(comblist) == 0:
    comblist = [
        int("".join(x)) for x in combinations_with_replacement(numlist, len(str(N)) - 1)
    ]
print(comblist)
print(comblist[-1])
"""
