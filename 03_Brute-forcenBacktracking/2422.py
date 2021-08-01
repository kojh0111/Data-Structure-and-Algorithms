"""
- 한윤정이 이탈리아에 가서 아이스크림을 사먹는데
메모리 초과 시간 초과...
그래서 전체 케이스에서 안되는 케이스들의 갯수를 제거
"""
import sys

input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
x_set = set()

for _ in range(M):
    a, b = [int(s) for s in input().split()]
    for i in range(1, N + 1):
        if i != a and i != b:
            x_set.add(tuple(sorted((a, b, i))))
# 모든 경우의 수 -> nC3 = int((N * (N - 1) * (N - 2)) / 6)
print(int((N * (N - 1) * (N - 2)) / 6) - len(x_set))

"""
from itertools import combinations
#시간 초과
input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
kinds = list("".join(c) for c in combinations([str(x + 1) for x in range(N)], 3))
for_remove = set()
for _ in range(M):
    a, b = [s for s in input().split()]
    for item in kinds:
        if (a in item) and (b in item):
            for_remove.add(item)

print(len(kinds))
"""

"""
from itertools import combinations
#메모리 초과
input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
combSet = set()
for _ in range(M):
    n, m = [int(x) for x in input().split()]
    items = [x + 1 for x in range(N)]
    items.remove(n)
    items.remove(m)
    print(items)
    combList = ["".join(str(comb)) for comb in combinations(items, 3)]
    combSet = {*combSet, *combList}

print(len(combSet))
"""
