"""
- K번째 수
이분탐색 문제/ 각 열별로 mid보다 작은 수 갯수를 파악하여 k보다 많아지면 답 출력
"""
import sys

input = sys.stdin.readline
N = int(input())
k = int(input())

left = 1
right = k

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    if cnt < k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)
