"""
- 문제집
위상절렬 문제/ 위상정렬을 풀 때는, 진입차수가 0인 정점을 큐에 삽입하고 간선 제거, 다시 반복하는 형태로 풀이
이 문제에서는 문제번호가 낮을수록 먼저 풀어야하므로 시작점은 번호가 낮은 문제 중 진입차수가 0인 정점에서 시작
"""
import sys
import heapq

input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
ans = list()

graph = [[] for _ in range(N + 1)]
inDegree = [0] * (N + 1)
queue = []

for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    inDegree[j] += 1

for i in range(1, N + 1):
    if inDegree[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    ans.append(tmp)
    for i in graph[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0:
            heapq.heappush(queue, i)

print(*ans)
