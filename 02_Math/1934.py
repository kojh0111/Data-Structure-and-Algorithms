"""
- 최소공배수
중학교 때 배운 a*b=l*g 이용
"""
from math import gcd
import sys

input = sys.stdin.readline
n = int(input().rstrip())

for _ in range(n):
    a, b = [int(x) for x in input().split()]
    print(int(a * b / gcd(a, b)))
