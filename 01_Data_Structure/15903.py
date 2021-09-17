"""
- 카드 합체 놀이
우선순위 큐를 활용하여 최소값들을 찾는 방식으로 해결
"""
import heapq

n, m = map(int, input().split())

lst = list(map(int, input().split()))
heap = []

for item in lst:
    heapq.heappush(heap, item)

for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a + b)
    heapq.heappush(heap, a + b)

print(sum(heap))
