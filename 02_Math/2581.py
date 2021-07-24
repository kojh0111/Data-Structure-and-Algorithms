"""
- 소수
에라토스테네스의 체를 이용하여 소수를 찾을 수 있음
python의 sum은 iterable을 인수로 받음
"""
a = int(input())
b = int(input())


def prime(n):
    n_sqrt = int(n ** 0.5) + 1
    prime_tf = [True] * (n + 1)
    for i in range(2, n_sqrt):
        if prime_tf[i]:
            for j in range(i * 2, n + 1, i):
                prime_tf[j] = False
    prime_num = [i for i in range(2, n + 1) if prime_tf[i]]
    return prime_num


need_num = list(filter(lambda x: x >= a, prime(b)))
if len(need_num):
    print(sum(need_num))
    print(need_num[0])
else:
    print(-1)
