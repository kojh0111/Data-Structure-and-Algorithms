"""
- 도영이가 만든 맛있는 음식
재료의 신맛과 쓴맛은 동시에 체크해야하므로 비트마스크를 활용하여 넣었을 때는 같이 계산 후 비교
"""
import sys

input = sys.stdin.readline

ans = sys.maxsize
sour = list()
bitter = list()
N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    sour.append(a)
    bitter.append(b)

for i in range(1, 1 << N):
    s, b = 1, 0
    for j in range(N):
        if i & 1 << j:
            s *= sour[j]
            b += bitter[j]
    ans = min(ans, abs(s - b))

print(ans)
