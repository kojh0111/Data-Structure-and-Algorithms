"""
- 문자열 집합
문제 이름과 같이 집합을 활용해야 함.
list 활용시 시간초과 했음
"""
import sys

input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
_set = {input().rstrip() for _ in range(N)}
cnt = 0

for _ in range(M):
    check = input().rstrip()
    if check in _set:
        cnt += 1

print(cnt)
