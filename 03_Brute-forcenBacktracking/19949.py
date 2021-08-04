"""
- 영재의 시험
백트랙킹 문제, 답을 입력할 조건에 맞게 풀면 됨
근데 시간이 너무 오래 걸림
일단 pypy3로 통과는 가능했음
"""
answer_sheet = [int(x) for x in input().split()]

cnt = 0


def recur(data):
    global cnt
    if len(data) == 10:
        score = 0
        for i in range(10):
            if data[i] == answer_sheet[i]:
                score += 1
        if score >= 5:
            cnt += 1
        return
    for i in range(1, 6):
        if (len(data) > 1) and data[len(data) - 2] == data[len(data) - 1] == i:
            # 같은 것이 3번 연속은 못 옴
            continue
        data.append(i)
        recur(data)
        data.pop()


recur([])
print(cnt)
