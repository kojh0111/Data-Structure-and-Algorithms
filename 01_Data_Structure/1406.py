"""
- 에디터
커서 위치를 기준으로 스택을 2개 구성
"""
import sys

input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = []

for _ in range(int(input().rstrip())):
    cmd = input().rstrip().split()
    if cmd[0] == "L":
        if str1:
            str2.append(str1.pop())
    elif cmd[0] == "D":
        if str2:
            str1.append(str2.pop())
    elif cmd[0] == "B":
        if str1:
            str1.pop()
    else:
        str1.append(cmd[1])

print("".join(str1 + str2[::-1]))
