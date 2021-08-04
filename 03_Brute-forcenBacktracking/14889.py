from itertools import combinations
import sys

input = sys.stdin.readline
N = int(input())
player = [x for x in range(N)]
arr = []
for i in range(N):
    arr.append([int(x) for x in input().split()])

ans = 999
team_cases = list(combinations(player, N // 2))
for start in team_cases:
    link = [x for x in player if x not in start]
    start_sum = 0
    link_sum = 0
    for i, j in list(combinations(start, 2)):
        start_sum += arr[i][j] + arr[j][i]
    for i, j in list(combinations(link, 2)):
        link_sum += arr[i][j] + arr[j][i]
    ans = min(abs(start_sum - link_sum), ans)

print(ans)
