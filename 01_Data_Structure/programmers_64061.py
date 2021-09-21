"""
프로그래머스
코딩테스트 연습 > 2021 카카오 개발자 겨울 인턴십 > 크레인 인형뽑기 게임
뽑아서 스택에 담고 담았을 때, 끝에 두개가 같다면 스택에서 제거
"""


def solution(board, moves):
    answer = [0]
    ans = 0

    for m in moves:
        m -= 1
        for i in range(len(board)):
            if board[i][m] != 0:
                answer.append(board[i][m])
                board[i][m] = 0
                if answer[-1] == answer[-2]:
                    answer.pop()
                    answer.pop()
                    ans += 2
                break
    return ans
