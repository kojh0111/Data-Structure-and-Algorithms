"""
- 카드 정렬하기
13975번과 같은 문제였지만, N이 1인 경우도 포함됨.
"""
import heapq

heap = []
N = int(input())
for _ in range(N):
    heapq.heappush(heap, int(input()))

ans = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    ans += a + b
    heapq.heappush(heap, a + b)
print(ans)
