"""
- N과 M (4)

"""
N, M = [int(x) for x in input().split()]


def recur(data, last):
    if len(data) == M:
        print(*data)
        return
    for i in range(last, N + 1):
        data.append(i)
        recur(data, i)
        data.pop()


recur([], 1)
