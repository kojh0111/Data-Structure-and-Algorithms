"""
- 기차가 어둠을 헤치고 은하수를
비트 마스킹 문제로 승객이 자리에 있으면 1, 없으면 0으로 놓고 비트마스크 연산을 실행
똑같은 모양은 건널 수 없으므로 다른 형태의 갯수만 세기 위해 set의 길이를 구함
"""
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

command = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
train = [0] * N

for i in range(M):
    if command[i][0] == 0:
        train[command[i][1]] = train[command[i][1]] | 1 << command[i][2]
    elif command[i][0] == 1:
        train[command[i][1]] = train[command[i][1]] & ~(1 << command[i][2])
    elif command[i][0] == 2:
        train[command[i][1]] = train[command[i][1]] << 1
        train[command[i][1]] = train[command[i][1]] & ~(1 << 20)
    elif command[i][0] == 3:
        train[command[i][1]] = train[command[i][1]] >> 1

print(len(set(train)))
