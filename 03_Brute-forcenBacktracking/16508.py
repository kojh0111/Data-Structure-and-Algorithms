"""
- 전공책
완전탐색 문제 -> 모든 케이스를 정리하고 각 값을 비교!
"""
import sys
from itertools import product

input = sys.stdin.readline
price = list()
title = list()

word = input().strip()
book_cnt = int(input())

for _ in range(book_cnt):
    p, t = input().split()
    price.append(int(p))
    title.append(t)

total = 1600001
cases = [x for x in product([0, 1], repeat=book_cnt)]  # 이 부분은 비트연산자로 해결하는 방법 연구할 필요가 있음


def check_word(titles, ans):
    for w in word:
        if w not in titles:
            return 1600001
        else:
            # 틀린 이유
            # "titles = " 이 부분이 없어서 titles를 replace한 titles가 반영이 안됨
            titles = titles.replace(w, "", 1)  # titles를 바꿔줘야 함! (replace한 값을 저장)
    return ans


for case in cases:
    titles = ""
    ans = 0
    for i in range(len(case)):
        if case[i] == 1:
            titles += title[i]
            ans += price[i]
    total = min(check_word(titles, ans), total)
    # print(case, titles, ans, check_word(titles, ans))

print(total if total != 1600001 else -1)
