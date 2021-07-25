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
