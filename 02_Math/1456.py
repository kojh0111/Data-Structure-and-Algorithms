"""
- 거의 소수
제곱(**) 연산
"""
a, b = (int(x) for x in input().split())
# b보다 작은 소수 찾기
b_sqrt = int(b ** 0.5) + 1
prime_tf = [True] * b_sqrt
for i in range(2, b_sqrt):
    if prime_tf[i]:
        for j in range(i * 2, b_sqrt, i):
            prime_tf[j] = False
prime_num = [i for i in range(2, b_sqrt) if prime_tf[i]]


def count_almost(n):
    n_list = []
    for i in prime_num:
        j = 2  # 여기서부터 거의 소수
        while True:
            if i ** j > n:
                break
            n_list.append(i ** j)
            j += 1

    return n_list


b_list = count_almost(b)  # b이하의 모든 거의 소수 찾기
a_list = count_almost(a - 1)  # a이상이라는 조건을 만족하려면 a미만을 제외
print(len(b_list) - len(a_list))

"""
from math import log

# 소수는 거의 소수는 아니므로 제외(a보다 작은 소수는 제거하지않으면 2번 제거하는 꼴이 됨)
need_num = list(filter(lambda x: x >= a, prime_num))
cnt = -len(need_num)

for p in prime_num:
    # b보다 작거나 같은 p의 제곱수 갯수(문제는 2제곱 이상이므로 먼저 빼줬음)
    cnt += int(log(b, p))
    # a보다 작은 p의 제곱수 갯수
    cnt -= int(log(a - 1, p)) if a != 1 else 0

print(cnt)
"""
