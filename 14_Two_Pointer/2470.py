N = int(input())
_list = [int(x) for x in input().split()]
_list.sort()

left = 0
right = len(_list) - 1

result = 10 ** 10
solution = []

while left != right:
    tmp = _list[left] + _list[right]
    if result > abs(tmp):
        solution = [_list[left], _list[right]]
        result = abs(tmp)
    if tmp > 0:
        right -= 1
    else:
        left += 1

print(*solution)
