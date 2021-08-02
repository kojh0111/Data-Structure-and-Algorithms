"""
- N과 M (4)
중복조합
"""
N, M = [int(x) for x in input().split()]


def recur(data, last):  # 조합은 크기 순으로만 해야하므로 구분이 필요
    if len(data) == M:
        print(*data)
        return
    for i in range(last, N + 1):
        data.append(i)
        recur(data, i)
        data.pop()


recur([], 1)
