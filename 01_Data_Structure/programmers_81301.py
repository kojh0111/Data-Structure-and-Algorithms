"""
프로그래머스
코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어
str의 replace method 활용
"""


def solution(s):
    _list = [
        ("0", "zero"),
        ("1", "one"),
        ("2", "two"),
        ("3", "three"),
        ("4", "four"),
        ("5", "five"),
        ("6", "six"),
        ("7", "seven"),
        ("8", "eight"),
        ("9", "nine"),
    ]
    for b, a in _list:
        s = s.replace(a, b)
    return int(s)
