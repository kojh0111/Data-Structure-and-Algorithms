"""
- 양팔저울
무게를 고를 수 있는 선택지는 3가지(더하거나 빼거나 안올리거나)에 대한 완전탐색
"""
k = int(input())
arr = [int(x) for x in input().split()]
weights = [0] * (3 ** 14)  # 집합을 만드는 것 보다 flag를 파악하는 방법이 더 빠르다
s = sum(arr)


def recur(idx, size):
    if idx == k:
        if size > 0:
            weights[size] = 1
    else:  # 3개의 함수를 실행... 이게 가능하구나...
        recur(idx + 1, size - arr[idx])
        recur(idx + 1, size)
        recur(idx + 1, size + arr[idx])


recur(0, 0)
print(s - sum(weights))

"""
k = int(input())
arr = [int(x) for x in input().split()]
weights = set()
s = sum(arr)


def recur(idx, size):
    if idx == k:
        weights.add(abs(size))
    else:
        recur(idx + 1, size - arr[idx])
        recur(idx + 1, size)
        recur(idx + 1, size + arr[idx])


recur(0, 0)
weights -= {0}
print(s - len(weights))
"""

"""
for test
13
18 20 9 17 3 12 10 8 16 2 7 19 5

"""
