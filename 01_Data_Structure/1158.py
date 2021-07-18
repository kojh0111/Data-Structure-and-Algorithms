"""
- 요세푸스 문제
deque 활용하기!
"""
from collections import deque

N, K = [int(x) for x in input().split()]
_list = [(x + 1) for x in range(N)]
ans = []

q = deque(_list)
for _ in range(N):
    q.rotate(-K)
    ans.append(str(q.pop()))

print("<" + ", ".join(ans) + ">")
