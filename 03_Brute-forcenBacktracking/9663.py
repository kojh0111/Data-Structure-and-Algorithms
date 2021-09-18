"""
- N-Queen
백트랙킹 문제
넣을 수 있는 숫자인지 판단하고 가능하다면 넣고 안되면 되돌리기
"""
N = int(input())
ans = 0


def solution(data):
    global ans
    if len(data) == N:
        ans += 1
        return
    for i in range(1, N + 1):
        for j in range(len(data)):
            if data[j] == i or len(data) - j == abs(i - data[j]):
                break
        else:
            data.append(i)
            solution(data)
            data.pop()


solution([])
print(ans)
