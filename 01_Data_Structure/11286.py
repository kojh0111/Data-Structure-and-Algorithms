"""
- 절댓값 힙
힙에 넣을 때 크기만 필요하지만 출력시 부호를 고려해야 하므로
힙은 tuple을 원소로 가질 수 있음을 이용하여 tuple에 부호를 넣기
"""
import sys  # input으로 했더니 틀림...
import heapq

input = sys.stdin.readline
N = int(input().rstrip())
heap = []
for _ in range(N):
    num = int(input().rstrip())
    if num != 0:
        heapq.heappush(
            heap, (abs(num), 1 if num > 0 else -1)
        )  # Heap elements can be tuples.
    else:
        try:
            elem = heapq.heappop(heap)
            print(elem[0] * elem[1])
        except IndexError:  # If the heap is empty, IndexError is raised.
            print(0)
