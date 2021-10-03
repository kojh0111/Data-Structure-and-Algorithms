import sys

input = sys.stdin.readline
N = int(input())
# _set = set(map(int, input().split()))
_list = sorted([int(x) for x in input().split()])
M = int(input())


# 이분 탐색을 모를 때,
# print(*[1 if dt in _set else 0 for dt in map(int, input().split())], sep="\n")

# 이분 탐색 활용
def bs(target):
    left = 0
    right = len(_list) - 1
    while left < right:
        mid = (left + right) // 2
        if _list[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return 1 if _list[left] == target else 0


_find = [int(x) for x in input().split()]

for dt in _find:
    print(bs(dt))
