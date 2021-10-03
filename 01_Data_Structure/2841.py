"""
- 외계인의 기타 연주
스택 문제
"""
import sys

input = sys.stdin.readline
N, P = [int(x) for x in input().split()]
lines = [[] for _ in range(7)]
ans = 0

for _ in range(N):
    line, flat = [int(x) for x in input().split()]
    if lines[line]:
        while lines[line] and lines[line][-1] > flat:
            ans += 1
            lines[line].pop()
        if lines[line] and lines[line][-1] == flat:
            continue
        else:
            lines[line].append(flat)
            ans += 1
    else:
        lines[line].append(flat)
        ans += 1

print(ans)
