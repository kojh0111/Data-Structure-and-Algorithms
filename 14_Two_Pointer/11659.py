"""
- 구간 합 구하기 4
먼저 처음부터 더하기를 하는 리스트를 완성하고(prefix_sum)
범위에 맞춰 차를 구해서 해결
"""
import sys

input = sys.stdin.readline
N, M = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
prefix_sum = [0]
for i in range(len(numbers)):
    prefix_sum.append(prefix_sum[-1] + numbers[i])

for i in range(M):
    x, y = [int(x) for x in input().split()]
    print(prefix_sum[y] - prefix_sum[x - 1])
