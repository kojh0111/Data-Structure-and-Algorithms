"""
- 스택 수열
FILO구조를 파악해 보기
"""
import sys

input = sys.stdin.readline
n = int(input())

_list = [int(i + 1) for i in range(n)]
stack = []
print_operator = ""
i = 1
for _ in range(n):
    num = int(input())
    if i <= num:
        while i <= num:
            stack.append(i)
            print_operator += "+"
            i += 1
        stack.pop()
        print_operator += "-"
    else:
        if num == stack[-1]:
            stack.pop()
            print_operator += "-"
        else:
            print("NO")
            quit()

for operator in print_operator:
    print(operator)
