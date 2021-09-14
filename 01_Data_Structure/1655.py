"""
- 가운데를 말해요
sort 사용시, O(n^2)으로 시간 부족
heapq 사용하여 풀이
"""
import heapq
import sys

input = sys.stdin.readline

N = int(input())
n = int(input())
print(n)
minhq, maxhq = [], [-n]

for _ in range(N - 1):
    n = int(input())
    if n > -maxhq[0]:
        heapq.heappush(minhq, n)
    else:
        heapq.heappush(maxhq, -n)

    if len(minhq) > len(maxhq):
        heapq.heappush(maxhq, -heapq.heappop(minhq))
    elif len(minhq) + 1 < len(maxhq):
        heapq.heappush(minhq, -heapq.heappop(maxhq))

    print(-maxhq[0])
