"""
- 쇠막대기
stack을 활용한 갯수 파악
"""
import sys

input = sys.stdin.readline

str = input()
str = str.replace("()", "z")

cnt = 0
stack = 0
for i in str:
    if i == "(":
        stack += 1
        cnt += 1
    elif i == ")":
        stack -= 1
    elif i == "z":
        cnt += stack

print(cnt)
