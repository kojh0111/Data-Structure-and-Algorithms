"""
- N과 M (1)
순열
"""
N, M = [int(x) for x in input().split()]


def recur(data):
    if len(data) == M:
        print(*data)
        return
    for i in range(1, N + 1):
        if i not in data:  # 중복을 허용하지 않음
            data.append(i)
            recur(data)
            data.pop()


recur([])
