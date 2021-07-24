"""
- 세 개의 소수 문제
골드바흐의 추측: 2 보다 큰 모든 짝수는 두 소수의 합으로 표현할 수 있다
골드바흐의 추측을 바탕으로 5 보다 큰 홀수를 세 소수의 합으로 표현가능
"""
import sys

input = sys.stdin.readline


def prime(n):  # 먼저 소수 찾기!
    prime_tf = [True] * (n)
    for i in range(2, int((n ** 0.5) + 1)):
        if prime_tf[i]:
            for j in range(i * 2, n, i):
                prime_tf[j] = False
    prime_num = [i for i in range(2, n) if prime_tf[i]]
    return prime_num


T = int(input())
for _ in range(T):
    odd = int(input())  # 어떤 경우든 1000이하에서는 표현가능
    prime_num = prime(odd)
    if odd - 4 in prime_num:  # 먼저 (2,2,소수) 꼴이면 끝!
        print(2, 2, odd - 4)
    else:  # odd보다 작지만 가장 큰 소수를 찾고 odd와의 간격이 2이면 (1,1,소수)의 꼴이 되므로 제외
        nottwo = (
            odd - prime_num[-1] if odd - prime_num[-1] != 2 else odd - prime_num[-2]
        )
        if (nottwo / 2) in prime_num:  # 간격의 절반이 소수라면 끝
            p1 = p2 = int(nottwo / 2)
        else:  # 간격의 절반이 소수가 아니라면 합이 nottwo가 되는 범위 내에서 둘 모두 소수인 경우 찾기
            p1 = p2 = int(nottwo / 2)
            while (p1 not in prime_num) or (p2 not in prime_num):
                for i in range(1, int(nottwo / 2)):
                    p1 = int(nottwo / 2) - i
                    p2 = int(nottwo / 2) + i
                    if (p1 in prime_num) and (p2 in prime_num):
                        break

        print(p1, p2, odd - nottwo)

"""
def three_primes(T):
    odd = T
    prime_num = prime(odd)
    if odd - 4 in prime_num:
        print(odd, 2, 2, odd - 4)
    else:
        nottwo = (
            odd - prime_num[-1] if odd - prime_num[-1] != 2 else odd - prime_num[-2]
        )
        if (nottwo / 2) in prime_num:
            p1 = p2 = int(nottwo / 2)
        else:
            p1 = p2 = int(nottwo / 2)
            while (p1 not in prime_num) or (p2 not in prime_num):
                for i in range(1, int(nottwo / 2)):
                    p1 = int(nottwo / 2) - i
                    p2 = int(nottwo / 2) + i
                    if (p1 in prime_num) and (p2 in prime_num):
                        break

        print(odd, p1, p2, odd - nottwo)


for i in range(3, 500):
    x = (i * 2) + 1
    three_primes(x)
"""
