"""
- 암호 만들기
조합 문제(N과 M 문제와 유사)
"""
L, C = [int(x) for x in input().split()]
alphabet = [x for x in input().split()]
alphabet.sort()

vowels = ["a", "e", "i", "o", "u"]


def recur(data, last):
    if len(data) == L:
        cnt = 0
        for v in vowels:
            if v in data:
                cnt += 1
        if 0 < cnt < L - 1:
            print(data)
        return
    for i in range(last, C):
        if alphabet[i] not in data:
            data += alphabet[i]
            recur(data, i)
            data = data[:-1]


recur("", 0)
