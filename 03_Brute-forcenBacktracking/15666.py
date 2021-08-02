"""
- N과 M (12)
중복을 허용하므로 무슨 숫자가 있는지 파악하고 순열 만들기
"""
N, M = [int(x) for x in input().split()]
nums = sorted(list(set([int(x) for x in input().split()])))


def recur(data, last):
    if len(data) == M:
        print(*data)
        return
    for i in range(last, len(nums)):
        data.append(nums[i])
        recur(data, i)
        data.pop()


recur([], 0)
