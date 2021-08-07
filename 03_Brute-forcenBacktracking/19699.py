"""
- 소-난다!
완전탐색 문제 / 소수 확인하고 없는 케이스 있는지 확인하고 출력
"""
from itertools import combinations

N, M = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]


def checkprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


ans = set()
for cb in list(combinations(arr, M)):
    if checkprime(sum(cb)):
        ans.add(sum(cb))

if ans:
    print(*sorted(ans))
else:
    print(-1)
