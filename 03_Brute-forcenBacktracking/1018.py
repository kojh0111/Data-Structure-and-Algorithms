"""
- 체스판 다시 칠하기
완전탐색 하기 모든 경우의 수가 1억보다 작을 때 가능
"""
N, M = [int(x) for x in input().split()]
data = [input() for i in range(N)]


def check(graph):
    b_ans, w_ans = 0, 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                if graph[i][j] == "B":
                    b_ans += 1
                else:
                    w_ans += 1
            else:
                if graph[i][j] == "W":
                    b_ans += 1
                else:
                    w_ans += 1
    return min(b_ans, w_ans)


ans = 64
for i in range(N - 7):
    for j in range(M - 7):
        graph = [data[x][j : j + 8] for x in range(i, i + 8)]
        ans = min(check(graph), ans)

print(ans)
