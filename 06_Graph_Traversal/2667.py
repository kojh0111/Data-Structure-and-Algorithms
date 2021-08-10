isize = 0


def dfs(x, y, pMap, visited):
    global isize
    visited[x][y] = 1
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    n = len(pMap)

    for d in di:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx > n - 1 or ny > n - 1:
            continue
        if pMap[nx][ny] == 0:
            continue
        if not visited[nx][ny]:
            isize += 1
            dfs(nx, ny, pMap, visited)


def cadastralSurvey(pMap):
    global isize
    visited = []
    n = len(pMap)

    for i in range(n):
        visited.append([0 for i in range(n)])

    num_island = 0
    islands_size = []

    for i in range(n):
        for j in range(n):
            if pMap[i][j] == 1 and visited[i][j] == 0:
                num_island += 1
                isize = 1
                dfs(i, j, pMap, visited)
                islands_size.append(isize)

    islands_size.sort()

    return num_island, islands_size


def read_input():
    size = int(input())
    returnMap = []
    for i in range(size):
        line = input()
        __line = []
        for j in range(len(line)):
            __line.append(int(line[j]))

        returnMap.append(__line)
    return returnMap


pMap = read_input()
(a, arr) = cadastralSurvey(pMap)

print(a)
print(*arr, sep="\n")


"""
N = int(input())
graph = [input() for i in range(N)]
cnt = []
visited = [[0] * N for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, number):
    visited[x][y] = number
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X >= N or Y < 0 or Y >= N:
            continue
        if not (visited[X][Y]) and graph[X][Y] == "1":
            dfs(X, Y, number)


for i in range(N):
    for j in range(N):
        if graph[i][j] == "1" and not (visited[i][j]):
            dfs(i, j, len(cnt) + 1)
            count = 0
            for i in range(N):
                count += visited[i].count(len(cnt) + 1)
            cnt.append(count)

print(len(cnt))
print(*sorted(cnt), sep="\n")
"""
