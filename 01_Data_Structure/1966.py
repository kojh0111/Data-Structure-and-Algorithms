"""
- 프린터 큐
우선순위가 같은 경우가 있어서 enumerate을 이용하여
각각의 인덱스를 메기고 순서에 맞춰서 pop
"""
import sys

input = sys.stdin.readline
N = int(input().rstrip())

for i in range(N):
    _, p = [int(x) for x in input().split()]
    docs_list = [int(x) for x in input().split()]
    docs_list = [(val, idx) for idx, val in enumerate(docs_list)]
    cnt = 0
    while True:
        if docs_list[0][0] == max(docs_list, key=lambda x: x[0])[0]:
            cnt += 1
            if docs_list[0][1] == p:
                print(cnt)
                break
            else:
                docs_list.pop(0)
        else:
            docs_list.append(docs_list.pop(0))
