"""
- 더하기 사이클
정수 나머지(%)와 몫(//) 연산
"""
N = n = input()
cnt = 0
while True:
    m = str((int(n) % 10) * 10 + (((int(n) // 10) + (int(n) % 10)) % 10))
    # 나머지를 이용하여 일의 자릿수를 구하고, 몫을 이용하여 십의 자릿수를 구함
    n = m
    cnt += 1

    if m == N:
        break

print(cnt)
