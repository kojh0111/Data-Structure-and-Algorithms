"""
- 근손실
백트랙킹 문제로 500보다 작아지면 버리고 500보다 큰 경우들만 찾고 카운트
"""
N, K = [int(x) for x in input().split()]
kits = [int(x) - K for x in input().split()]  # 항상 K씩 빠지므로 먼저 빼놓고 계산

cnt = 0


def recur(weight, data):
    global cnt
    if len(data) == N:
        cnt += 1
        return
    for i in range(len(kits)):
        if weight < 500:
            continue
        if i not in data:
            data.append(i)
            weight += kits[i]
            recur(weight, data)
            weight -= kits[data[-1]]  # 뺄 때 무게도 같이 빼줘야 무게 변동 확인 가능
            data.pop()


recur(500, [])
print(cnt)
