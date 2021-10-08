"""
- 상근이의 여행
이 문제는 연결그래프가 주어졌고
비행기의 종류를 구하늠 문제이므로 국가 수 - 1이 답임
"""
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        nothing = input()
    print(N - 1)
