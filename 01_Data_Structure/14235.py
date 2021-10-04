"""
- 크리스마스 선물
우선순위 큐 문제로 최대힙 활용
"""
import heapq
import sys

input = sys.stdin.readline
N = int(input())
que = list()
for _ in range(N):
    cmd = list(map(int, input().rstrip().split()))
    if cmd[0] == 0:
        if que:
            print(-heapq.heappop(que))
        else:
            print(-1)
    else:
        for i in range(cmd[0]):
            heapq.heappush(que, -cmd[i + 1])
