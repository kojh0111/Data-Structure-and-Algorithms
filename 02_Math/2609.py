"""
- 최대공약수와 최소공배수
python에는 gcd, lcm이 존재!
"""
from math import gcd, lcm
import sys

input = sys.stdin.readline
a, b = [int(x) for x in input().split()]
d = gcd(a, b)
m = lcm(a, b)
print(d)
print(m)
"""
def gcd(m, n):
    if m < n:
        (m, n) = (n, m)
    if (m % n) == 0:
        return n
    else:
        return gcd(n, m % n)
a * b = l * g 성질 이용
"""
