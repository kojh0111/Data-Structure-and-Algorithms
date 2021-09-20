"""
- 파일 합치기 3
우선순위 큐를 활용하여 작은 파일 두 개를 빼서 더한 후 다시 우선순위 큐에 담는 과정을 크기가 1이 될 때까지 반복
"""
import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    heap = []

    for i in lst:
        heapq.heappush(heap, i)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        ans += a + b
        heapq.heappush(heap, a + b)

    print(ans)
