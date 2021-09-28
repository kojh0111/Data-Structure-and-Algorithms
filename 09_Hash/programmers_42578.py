from collections import Counter


def solution(clothes):

    count_dict = Counter([kind for _, kind in clothes])
    ans = 1
    for value in count_dict.values():
        ans *= value + 1

    return ans - 1
