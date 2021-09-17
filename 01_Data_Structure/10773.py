"""
- 제로
스택 문제
"""
lst = list()
for _ in range(int(input())):
    n = int(input())
    if n == 0:
        lst.pop()
    else:
        lst.append(n)

print(sum(lst))
