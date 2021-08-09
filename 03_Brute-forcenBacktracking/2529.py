"""
- 부등호
백트랙킹 문제로 접근
부등호를 만족하지 않으면 stop,
만족하는 모든 경우 중 맨 앞과 맨 뒤가 가장 작은 수와 가장 큰 수
"""
N = int(input())
op = [x for x in input().split()]
visited = [0] * 10
possible = []


def recur(data):
    if len(data) == N + 1:
        possible.append(data)
        return
    for i in range(10):
        if visited[i] == 0:
            if len(data) == 0 or eval(data[-1] + op[len(data) - 1] + str(i)):
                visited[i] = 1
                data += str(i)
                recur(data)
                visited[i] = 0
                data = data[:-1]


recur("")
print(possible[-1])
print(possible[0])
