"""
- 회의실 배정
많은 회의를 하기 위해서는, 끝나는대로 회의를 시작하게 하면 됨! (모든 경우를 할 필요가 없고 순서대로 넣어서 확인하면 되므로 그리디 문제임을 파악)
"""
import sys
from operator import itemgetter

input = sys.stdin.readline
N = int(input())
meetings = list()
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))
# sorted를 할 때, 다중 수준의 정렬이 가능!
meetings = sorted(meetings, key=itemgetter(1, 0))
# meetings = sorted(meetings, key=lambda x: (x[1], x[0]))   # 위에 함수와 같게 작용

t = 0
ans = 0
for s, e in meetings:
    if s >= t:
        ans += 1
        t = e

print(ans)
