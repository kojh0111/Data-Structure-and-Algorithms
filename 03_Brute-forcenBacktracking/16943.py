"""
- 숫자 재배치
permutations을 이용해 간단히 풀이 가능
"""
from itertools import permutations

a, b = [x for x in input().split()]


def solve(a, b):
    if len(a) > len(b):
        print(-1)
        return

    comblist = [
        int("".join(x))
        for x in permutations([s for s in a], len(a))
        if int("".join(x)) < int(b)
    ]
    if len(comblist) == 0:
        print(-1)
    elif len(str(max(comblist))) != len(a):
        print(-1)
    else:
        print(max(comblist))


solve(a, b)
