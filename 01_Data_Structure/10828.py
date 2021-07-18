"""
- 스택
리스트를 이용하여 스택 만들어보기
"""
import sys

myStack = []
input = sys.stdin.readline

n = int(input())
for i in range(n):
    temp = [x for x in input().split()]
    func = temp[0]
    if func == "push":
        myStack.append(temp[1])
    elif func == "pop":
        if len(myStack) != 0:
            print(myStack.pop())
        else:
            print(-1)
    elif func == "size":
        print(len(myStack))
    elif func == "empty":
        if len(myStack) != 0:
            print(0)
        else:
            print(1)
    elif func == "top":
        if len(myStack) != 0:
            print(myStack[-1])
        else:
            print(-1)
