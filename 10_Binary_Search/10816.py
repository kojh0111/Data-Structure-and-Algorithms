"""
- 숫자 카드 2
내장 함수를 이용해 쉽게 풀이함
"""
from collections import Counter
import sys

input = sys.stdin.readline
N = int(input())
n = [int(x) for x in input().split()]
M = int(input())
m = [int(x) for x in input().split()]
n_count = Counter(n)

ans = [n_count[i] for i in m]
print(*ans)
