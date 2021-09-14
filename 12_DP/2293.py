"""
- 동전 1

"""
n, k = [int(x) for x in input().split()]
nums = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in nums:
    for j in range(1, k+1):
        if j-i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
