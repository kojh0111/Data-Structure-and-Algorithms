"""
- 동전 0
이 문제는 배수관계에 있으므로 큰 것부터 제거해 가는 것이 가능 -> 그리디임을 판별가능!
"""
import sys

input = sys.stdin.readline
N, K = [int(x) for x in input().split()]
coins = sorted([int(input()) for _ in range(N)], reverse=True)

ans = 0
for coin in coins:
    ans += K // coin
    K -= coin * (K // coin)

print(ans)
