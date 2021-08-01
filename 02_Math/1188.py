"""
- 음식 평론가
나누는 기준이 최대공약수임을 이용
"""
from math import gcd

n, m = [int(x) for x in input().split()]
print(m - gcd(n, m))
