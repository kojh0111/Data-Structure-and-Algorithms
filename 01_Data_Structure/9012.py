"""
- 괄호
스택의 대표 예시로 스택을 이용해 풀어도 되지만...(주석처리)
그냥 숫자로 푸는게 더 빠름!
"""
import sys

"""
def checkParen(p):
    stack = []
    for c in p:
        if c == "(":
            stack.append(c)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    if len(stack) == 0:
        return "YES"
    else:
        return "NO"
"""

input = sys.stdin.readline
n = int(input())
result = ""
for _ in range(n):
    p = input().rstrip()
    # print(checkParen(p))
    cnt = 0
    for c in p:
        cnt += 1 if c == "(" else -1
        if cnt < 0:
            break

    result += "YES\n" if cnt == 0 else "NO\n"

print(result)
