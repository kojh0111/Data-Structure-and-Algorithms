"""
- 강의실
끝나는 시간을 기준으로 heapq를 생성
끝나기 전에 시작해야하는 강의가 있다면 강의실으 더 필요한 것이 되므로 끝나는 시간을 비교하는 것으로 충분
"""
import heapq
import sys

input = sys.stdin.readline
table = list()
N = int(input())
for _ in range(N):
    _, s, e = map(int, input().split())
    table.append((s, e))
table.sort()

heap = []
heapq.heappush(heap, table[0][1])

for i in range(1, N):
    s, e = table[i]
    if heap[0] > s:
        # 새로운 강의실 추가됨(끝나는 시간이 추가됨)
        heapq.heappush(heap, e)
    else:
        # 원래 강의실에 다음 수업을 넣기(끝나는 시간이 바뀜)
        heapq.heappop(heap)
        heapq.heappush(heap, e)

print(len(heap))
