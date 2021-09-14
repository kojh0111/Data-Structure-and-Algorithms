"""
- 동전 2
하나만을 이용해서 만들 수 있는 숫자를 먼저 체크하고
나머지 숫자들도 만들 수 있는지 여부를 체크하면 끝!
"""
n, k = [int(x) for x in input().split()]
nums = sorted([int(input()) for _ in range(n)])

dp = [10001 for _ in range(k + 1)]

for num in nums:
    # k 보다 큰 수가 입력될 경우 제외
    if num <= k:
        dp[num] = 1

for i in range(nums[0] + 1, k + 1):
    for num in nums:
        # i라는 숫자를 만들 수 있는지 체크
        if i - num >= 0:
            # i-num이라는 숫자를 만들 수 있는지 체크
            dp[i] = min(dp[i], dp[i - num] + 1)

if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])
