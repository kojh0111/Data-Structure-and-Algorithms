"""
- 덱
deque 활용하기!
"""
import sys
from collections import deque

input = sys.stdin.readline
myQueue = deque()
n = int(input())
for i in range(n):
    temp = [x for x in input().split()]
    func = temp[0]
    if func == "push_back":
        myQueue.append(temp[1])
    elif func == "push_front":
        myQueue.appendleft(temp[1])
    elif func == "pop_front":
        if myQueue:
            print(myQueue.popleft())
        else:
            print(-1)
    elif func == "pop_back":
        if myQueue:
            print(myQueue.pop())
        else:
            print(-1)
    elif func == "size":
        print(len(myQueue))
    elif func == "empty":
        if myQueue:
            print(0)
        else:
            print(1)
    elif func == "front":
        if myQueue:
            print(myQueue[0])
        else:
            print(-1)
    elif func == "back":
        if myQueue:
            print(myQueue[-1])
        else:
            print(-1)
