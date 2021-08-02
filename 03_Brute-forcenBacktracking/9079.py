"""
- 동전 게임
완전 탐색을 위해 모든 경우의 수를 구해봄
모든 경우의 수가 2^8 = 64 이므로 충분히 가능
모든 경우의 수를 product로 구함
"""
import sys
from itertools import product

input = sys.stdin.readline
all_cases = list(product([0, 1], repeat=8))


def flip(matrix):
    global ans
    for case in all_cases:
        copy_matrix = [row[:] for row in matrix]  # 여기가 이해가 안됨
        # copy_matrix = [row for row in matrix] # 이 경우에는 copy_matrix가 바뀜
        # print(copy_matrix, case)
        if ans < sum(case):
            continue
        for i in range(3):
            if case[i] == 1:
                for j in range(3):
                    copy_matrix[i][j] = (copy_matrix[i][j] + 1) % 2
        for i in range(3):
            if case[i + 3] == 1:
                for j in range(3):
                    copy_matrix[j][i] = (copy_matrix[j][i] + 1) % 2
        if case[6] == 1:
            for i in range(3):
                copy_matrix[i][i] = (copy_matrix[i][i] + 1) % 2
        if case[7] == 1:
            for i in range(3):
                copy_matrix[i][2 - i] = (copy_matrix[i][2 - i] + 1) % 2

        check_all = sum(list(map(sum, copy_matrix)))
        if check_all == 9 or check_all == 0:
            ans = sum(case)


N = int(input())
for _ in range(N):
    matrix = []
    ans = 9
    for _ in range(3):
        matrix.append([1 if x == "T" else 0 for x in input().split()])

    flip(matrix)
    print(-1 if ans == 9 else ans)

"""
N = int(input())
for _ in range(N):
    matrix = []
    min_ans = 9
    for _ in range(3):
        matrix.append(input().split())
    for case in all_cases:
        print(case, matrix)
        # case[0] case[1] case[2] 가 1 이면 flip_row(0) flip_row(1) flip_row(2)
        if case[0] == 1:
            flip_row(0)
        if case[1] == 1:
            flip_row(1)
        if case[2] == 1:
            flip_row(2)
        # case[3] case[4] case[5] 가 1 이면 flip_col(0) flip_col(1) flip_col(2)
        if case[3] == 1:
            flip_col(0)
        if case[4] == 1:
            flip_col(1)
        if case[5] == 1:
            flip_col(2)
        # case[6] case[7] 가 1 이면 flip_ru() flip_lu()
        if case[6] == 1:
            for i in range(3):
                matrix[i][2 - i] = "H" if matrix[i][2 - i] == "T" else "T"
        if case[7] == 1:
            for i in range(3):
                matrix[i][i] = "H" if matrix[i][i] == "T" else "T"

        if (matrix == [["T", "T", "T"], ["T", "T", "T"], ["T", "T", "T"]]) or (
            matrix == [["H", "H", "H"], ["H", "H", "H"], ["H", "H", "H"]]
        ):
            print(case, matrix)
            min_ans = sum(case) if (sum(case) < min_ans) else min_ans
    if min_ans == 9:
        print(-1)
    else:
        print(min_ans)
"""
"""
    1
    H H H
    H T H
    H H H
=> 3 도대체 왜!!!!!
"""
