"""
- 카드2
deque 활용하기!(요세푸스 문제와 비슷했음)
"""
from collections import deque

_list = [int(x + 1) for x in range(int(input()))]
cards = deque(_list)
for _ in range(len(_list) - 1):
    cards.popleft()
    cards.rotate(-1)

print(cards[0])
