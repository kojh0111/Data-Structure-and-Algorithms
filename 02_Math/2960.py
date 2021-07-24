"""
- 에라토스테네스의 체
소수 찾는 방법
"""
n, k = [int(x) for x in input().split()]
cnt = 0
prime_tf = [True] * (n + 1)
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if prime_tf[j]:
            prime_tf[j] = False
            cnt += 1
            if cnt == k:
                print(j)
