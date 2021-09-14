"""
- AC
deque을 활용, 뒤집는 과정을 반대쪽에서 pop을 하는 방법으로 해결!
"""
import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    func = input().rstrip()
    z = input().rstrip()
    test = input().rstrip().strip("[]")
    dq = deque(test.replace(",", " ").split())

    flag = 0
    for c in func:
        if c == "D":
            if len(dq) == 0:
                print("error")
                break
            dq.popleft() if flag == 0 else dq.pop()
        else:
            flag = 1 - flag

    else:
        print("[" + ",".join(list(dq)) + "]") if flag == 0 else print(
            "[" + ",".join(list(dq)[::-1]) + "]"
        )
