"""
- 최소 회의실 개수
1374번과 완전 동일
"""
import heapq
import sys

input = sys.stdin.readline
table = list()
N = int(input())
for _ in range(N):
    s, e = map(int, input().split())
    table.append((s, e))
table.sort()

heap = []
heapq.heappush(heap, table[0][1])

for i in range(1, N):
    s, e = table[i]
    if heap[0] > s:
        heapq.heappush(heap, e)
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, e)

print(len(heap))
