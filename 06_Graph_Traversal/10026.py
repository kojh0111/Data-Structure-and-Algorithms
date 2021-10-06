"""
- 적록색약
그래프 탐색으로 2가지로 나눠서 진행
"""
import sys
from collections import deque

sys.setrecursionlimit(100000)
input = sys.stdin.readline
N = int(input())
matrix = [list(input()) for _ in range(N)]
matrix_rb = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if matrix[i][j] == "R" or matrix[i][j] == "G":
            matrix_rb[i][j] = "R"
        else:
            matrix_rb[i][j] = "B"


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
count_rb = 0


def graph(x, y, c, matrix):
    q = deque()
    q.append([x, y, matrix[x][y]])
    matrix[x][y] = 0
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if X < 0 or X >= N or Y < 0 or Y >= N:
                continue
            if matrix[X][Y] == c:
                matrix[X][Y] = 0
                q.append([X, Y, c])


for i in range(N):
    for j in range(N):
        if matrix[i][j] != 0:
            graph(i, j, matrix[i][j], matrix)
            count += 1
        if matrix_rb[i][j] != 0:
            graph(i, j, matrix_rb[i][j], matrix_rb)
            count_rb += 1

print(count, count_rb)
