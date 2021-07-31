"""
- 영화감독 숌
666부터 666이 들어있는 모든 숫자를 체크하기
"""
num = 666
cnt = 1

n = int(input())
while cnt != n:
    num += 1
    if "666" in str(num):
        cnt += 1
if cnt == n:
    print(num)

"""
다른 풀이
N = int(input())

for i in range(666, int(1e9)):
    if "666" in str(i):
        N -= 1
        if N == 0:
            print(i)  # N번째 숫자 찾음 -> 끝
            exit()
"""
