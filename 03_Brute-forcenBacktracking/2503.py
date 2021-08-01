"""
- 숫자 야구
해당하는 케이스를 확인하는 작업이 필요
remove 해서 남은 원소 파악하기
그러나 remove를 하면 인덱스가 조정이 된다는 사실을 인지하고
remove 후 인덱스를 옮겨야함
"""
from itertools import permutations

num_list = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
N = int(input())
# asdf = []

for _ in range(N):
    test, s, b = [int(x) for x in input().split()]
    test = tuple(int(x) for x in str(test))
    x_cnt = 0  # remove를 하고나서 건너뛰는 원소를 놓치지 않기 위함, "#"로 확인가능
    for i in range(len(num_list)):
        s_cnt, b_cnt = 0, 0
        i -= x_cnt
        # asdf.append((i, num_list[i]))
        for j in range(3):
            if test[j] in num_list[i]:
                if test[j] == num_list[i][j]:
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            num_list.remove(num_list[i])
            x_cnt += 1
# print(asdf)
print(len(num_list))

"""
for _ in range(N):
    test, s, b = [int(x) for x in input().split()]
    test = tuple(int(x) for x in str(test))
    for num in num_list:
        s_cnt, b_cnt = 0, 0
        for i in range(3):
            if test[i] in num:
                if test[i] == num[i]:
                    s_cnt += 1
                else:
                    b_cnt += 1
        if s_cnt != s or b_cnt != b:
            num_list.remove(num)

print(len(num_list))
"""
