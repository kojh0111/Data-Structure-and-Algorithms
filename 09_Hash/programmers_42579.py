"""
- 베스트앨범
일단 인덱스를 매기고 장르별 순위를 구하기 그 다음 장르별로 최대 2개까지 인덱스를 찾고 ans에 추가
"""
from operator import itemgetter


def solution(genres, plays):
    zip_list = sorted(
        list([idx, *val] for idx, val in enumerate(zip(genres, plays))),
        key=itemgetter(1, 2),
        reverse=True,
    )
    gen = list(set(genres))
    sum_gen = [0] * len(gen)
    for i in range(len(gen)):
        for song in zip_list:
            if song[1] == gen[i]:
                sum_gen[i] += song[2]

    sort_gen = [x[1] for x in sorted(list(zip(sum_gen, gen)), reverse=True)]

    ans = list()
    for genre in sort_gen:
        two_max = []
        for song in zip_list:
            if song[1] == genre:
                if len(two_max) < 2:
                    two_max.append(song[0])
                    ans.append(song[0])
                else:
                    break

    return ans
