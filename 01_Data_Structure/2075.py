"""
- N번째 큰 수
heap에는 N개의 수만 유지, 마지막까지 넣고 가장 작은 수 찾기
"""
import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = list()

for _ in range(N):
    for i in [int(x) for x in input().split()]:
        if len(heap) < N:
            heapq.heappush(heap, i)
        else:
            heapq.heappush(heap, i)
            heapq.heappop(heap)

print(heap[0])

# 메모리 초과
# for _ in range(N):
#     heap.extend([int(x) for x in input().split()])

# ans = heapq.nlargest(N, heap)
# print(ans[-1])
