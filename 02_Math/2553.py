"""
- 팩토리얼?
원래 팩토리얼 구하듯이 곱하면 숫자가 너무 커져서 에러..
그래서 패턴을 찾을 필요가 있음(사진-반복된 패턴을 찾음 https://www.icloud.com/iclouddrive/0O4Opw6tQKVXuw7b6r9VHTB-g#boj_2553)
"""
from functools import reduce

n = int(input())

# 5의 배수가 없으면 반복적인 패턴이 있음
num = [x % 10 for x in range(1, n + 1) if x % 5 != 0]

if n >= 5:  # 5의 배수들은 따로 곱하기
    num += [x for x in range(1, n + 1) if x % 5 == 0]
num_multiply = reduce(lambda a, b: a * b, num)
ans = str(num_multiply).rstrip("0")[-1]  # 0이 아닌 숫자 찾기
print(ans)

"""
def f(n):
    num = 1
    if n < 2:
        return num
    else:
        return n * f(n - 1)

print(str(f(n)).rstrip("0")[-1])
"""
