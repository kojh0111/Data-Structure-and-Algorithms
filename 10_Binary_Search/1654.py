"""
- 랜선 자르기
2 ** 31 이라는 숫자는 완전 탐색이 불가능하다는 사실을 바탕으로 이분탐색을 고려해봐야 하다는 추정이 가능
"""
import sys

input = sys.stdin.readline
K, N = [int(x) for x in input().split()]
_list = [int(input()) for _ in range(K)]


def lancable(long):
    n = 0
    for cable in _list:
        n += cable // long
    return n


left, right = 0, 2 ** 31
ans = 0
while left <= right:
    mid = (left + right) // 2
    if lancable(mid) < N:
        right = mid - 1
    else:
        left = mid + 1
        ans = max(ans, mid)

print(ans)
