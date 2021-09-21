"""
- 부분수열의 합
완전탐색을 활용하여 풀이/ 모든 케이스를 구하고 없는 숫자를 차근차근 구하기
"""
import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
arr = [int(x) for x in input().split()]

sum_set = set()
for i in range(1, n + 1):
    arr_comb = combinations(arr, i)
    for a in arr_comb:
        sum_set.add(sum(a))

for i in range(1, 2 ** n + 1):
    if i not in sum_set:
        print(i)
        break
