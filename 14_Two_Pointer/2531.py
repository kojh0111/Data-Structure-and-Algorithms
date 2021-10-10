"""
- 회전 초밥
Sliding Window 문제
left와 right 간격이 일정하게 증가
이 문제에서는 회전 초밥으로 1차원 배열처럼 안보이지만
회전을 2번 반복시켜 1차원 배령로 만들 수 있으므로 투포인터로 풀이 가능!
"""
import sys
from collections import defaultdict

input = sys.stdin.readline
N, d, k, c = [int(x) for x in input().split()]
sushi = [int(input()) for _ in range(N)]
sushi += sushi

kinds = defaultdict(int)
kinds[c] = 1

left, right = 0, 0

while right - left != k:
    kinds[sushi[right]] += 1
    right += 1

ans = len(kinds)

while right != len(sushi):
    ans = max(ans, len(kinds))
    kinds[sushi[left]] -= 1
    if kinds[sushi[left]] == 0:
        del kinds[sushi[left]]
    kinds[sushi[right]] += 1

    left += 1
    right += 1

print(ans)
