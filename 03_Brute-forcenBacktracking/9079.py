# fail
import sys
from itertools import product

input = sys.stdin.readline
all_cases = list(product([0, 1], repeat=8))


def flip_row(i):
    for j in range(3):
        matrix[i][j] = "H" if matrix[i][j] == "T" else "T"


def flip_col(j):
    for i in range(3):
        matrix[i][j] = "H" if matrix[i][j] == "T" else "T"


def for_case(matrix, case):
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
    return matrix


N = int(input())
for _ in range(N):
    matrix = []
    min_ans = 9
    for _ in range(3):
        matrix.append(input().split())
    append_finished = matrix
    print(append_finished)
    for case in all_cases:
        print(case, append_finished)
        matrix = for_case(append_finished, case)
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
