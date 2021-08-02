"""
- N과 M (9)
같은 숫자를 포함하고 있으므로 갯수를 파악해서 갯수가 0이 되면 멈춤
"""
from collections import Counter

N, M = [int(x) for x in input().split()]
nums = sorted([int(x) for x in input().split()])
num, cnt = map(list, zip(*list(Counter(nums).items())))


def recur(data):
    if len(data) == M:
        print(*data)
        return
    for i in range(len(cnt)):
        if cnt[i]:
            cnt[i] -= 1
            data.append(num[i])
            recur(data)
            data.pop()
            cnt[i] += 1


recur([])
