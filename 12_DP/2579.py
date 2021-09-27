"""
- 계단 오르기
연속해서 오를 수 없는 부분은 따로 계산하고 순차적으로 한칸 씩 더 올라가면서 점수의 최댓값을 누적시킴
"""
import sys

input = sys.stdin.readline
n = int(input())
steps = [int(input()) for _ in range(n)]
dp = [steps[0]]

try:
    dp.append(max(steps[1], steps[0] + steps[1]))
except IndexError:
    pass

try:
    dp.append(max(steps[1] + steps[2], steps[0] + steps[2]))
except IndexError:
    pass

for i in range(3, n):
    dp.append(max(steps[i] + dp[i - 2], steps[i] + steps[i - 1] + dp[i - 3]))

print(dp[-1])
