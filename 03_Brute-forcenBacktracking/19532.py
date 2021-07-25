"""
- 수학은 비대면강의입니다
2가지 방법
1. 숫자가 -999 ~ 999 사이이므로 다 대입
2. 역행렬을 이용한 행렬 계산
"""
import sys

input = sys.stdin.readline
a, b, c, d, e, f = [int(x) for x in input().split()]

print(
    int(((c * e) - (b * f)) / ((a * e) - (b * d))),
    int(((a * f) - (c * d)) / ((a * e) - (b * d))),
)
"""
# Brute Force
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a * x + b * y == c) and (d * x + e * y == f):
            print(x, y)
            break
"""
"""
# Numpy의 행렬연산
import numpy as np

v1 = np.array([[a, b], [d, e]])
v2 = np.array([[c], [f]])
print(type(*np.linalg.inv(v1).dot(v2)[:, 0]))
"""
