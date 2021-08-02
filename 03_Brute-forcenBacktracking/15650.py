"""
- N과 M (2)
조합
"""
N, M = [int(x) for x in input().split()]


def recur(data, last):  # 크기 순으로만!
    if len(data) == M:
        print(*data)
        return
    for i in range(last + 1, N + 1):
        if i not in data:
            data.append(i)
            recur(data, i)
            data.pop()


recur([], 0)
