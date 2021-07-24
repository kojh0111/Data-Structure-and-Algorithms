"""
- 폰 호석만
Python에서 10진수로 만드는 내장함수가 존재(int(x,base))
"""
from string import ascii_lowercase, digits

numeral = {"0": 2}  # 1진법은 없음(int(num,1)이 안되니까 0만 있는 숫자를 대비하여 넣어둠)
for i in range(len(digits) - 1):  # 2진법에서는 0,1 6진법은 0~5
    numeral[digits[i + 1]] = i + 2

for i in range(len(ascii_lowercase)):  # a는 10을 의미하므로 a가 있으면 11진법 이상
    numeral[ascii_lowercase[i]] = i + 11

a, b = [x for x in input().split()]
f_numeral = [c for c in a]  # 각각에 대한 가장 큰 값 찾기
r_numeral = [c for c in b]

f_max = 2
for c in f_numeral:
    if f_max < numeral[c]:
        f_max = numeral[c]

r_max = 2
for c in r_numeral:
    if r_max < numeral[c]:
        r_max = numeral[c]

cases = []  # 케이스의 갯수에 따라 출력값이 다름
for f in range(f_max, 37):
    for r in range(r_max, 37):
        if int(a, f) == int(b, r):
            if f == r:
                continue
            if int(a, f) >= 2 ** 63:
                continue
            else:
                cases.append((int(a, f), f, r))

if len(cases) == 0:
    print("Impossible")
elif len(cases) == 1:
    print(cases[0][0], cases[0][1], cases[0][2])
else:
    print("Multiple")
