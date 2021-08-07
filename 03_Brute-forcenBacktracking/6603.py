"""
- 로또
list unpacking을 활용했고, 백트래킹 문제였으나 combinations로 간단히 풀이 가능
"""
from itertools import combinations

while True:
    t = [int(x) for x in input().split()]
    if 0 in t:
        break
    _, *arr = t
    for cb in list(combinations(arr, 6)):
        print(*cb)
    print()
