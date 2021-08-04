N, K = [int(x) for x in input().split()]
kits = [int(x) - K for x in input().split()]

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
            weight -= kits[data[-1]]
            data.pop()


recur(500, [])
print(cnt)
