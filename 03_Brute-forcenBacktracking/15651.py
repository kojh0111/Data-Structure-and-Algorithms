"""
- N과 M (3)

"""
N, M = [int(x) for x in input().split()]


def recur(data):
    if len(data) == M:
        print(*data)
        return
    for i in range(1, N + 1):
        data.append(i)
        recur(data)
        data.pop()


recur([])