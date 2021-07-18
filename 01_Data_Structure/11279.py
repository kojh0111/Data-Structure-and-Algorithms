"""
- 최대 힙
원래 힙은 최솟값이 활용되므로 음수로 만들어서 힙을 구성하고
출력할 때 다시 '-'를 붙임으로 원래 수로 만듦
"""

import sys
import heapq

input = sys.stdin.readline
N = int(input().rstrip())

heap = []

for _ in range(N):
    num = int(input().rstrip())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        try:
            print(-(heapq.heappop(heap)))
        except IndexError:
            print(0)
