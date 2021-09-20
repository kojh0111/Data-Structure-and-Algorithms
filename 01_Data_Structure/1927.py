"""
- 최소 힙
파이썬 heapq를 활용!
"""
import sys
import heapq

input = sys.stdin.readline
heap = list()

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
