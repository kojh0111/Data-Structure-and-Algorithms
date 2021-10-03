"""
- 숫자 카드 2
내장 함수를 이용해 쉽게 풀이함
이분 탐색을 이용한 풀이 - 이 문제는 bisect라는 내장모듈을 활용해 봄!
"""
# from collections import Counter
import bisect
import sys

input = sys.stdin.readline
N = int(input())
n = [int(x) for x in input().split()]
M = int(input())
m = [int(x) for x in input().split()]
# n_count = Counter(n)

# ans = [n_count[i] for i in m]
# print(*ans)

# 이분 탐색으로 풀어보기!!
n.sort()
print(
    *[(bisect.bisect_right(n, target) - bisect.bisect_left(n, target)) for target in m]
)
