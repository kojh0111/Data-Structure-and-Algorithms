"""
- 부분수열의 합
완전탐색으로 풀이 / combinations를 이용해 모든 경우를 구해서 더함
"""
from itertools import combinations

N, S = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

cnt = 0
for i in range(1, N + 1):
    all_cases = []
    all_cases = list(combinations(arr, i))
    for case in all_cases:
        if sum(case) == S:
            cnt += 1

print(cnt)
