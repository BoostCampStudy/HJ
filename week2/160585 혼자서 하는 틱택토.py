# result
#   correctness: 100.0
# approach
#   0이 반환되는 경우: O나 X가 자신의 차례를 이긴 경우
#   1. xcnt가 ocnt 보다 많은 경우와 ocnt가 xcnt보다 한 개 초과 많은 경우
#   2. O가 이겼는데 ocnt가 xcnt보다 하나 많지 않을 때 ex. ["OOO", "X.X", "X.."]
#   4. X가 이겼는데 ocnt와 xcnt가 같지 않을 때 ex. ["XXX", "OO.", "O.O"]

def is_win(k, board):
    line = k + k + k
    for i in range(3):
        if board[i] == line:
            return True

    for j in range(3):
        if board[0][j] == k:
            flag = True
            for x in range(3):
                if board[x][j] != k:
                    flag = False
                    break
            if flag:
                return True

    if board[1][1] == k and \
            ((board[0][0] == k and board[2][2] == k) or \
             (board[0][2] == k and board[2][0] == k)):
        return True

    return False


def solution(board):
    ocnt = xcnt = 0
    for i in range(3):
        ocnt += board[i].count('O')
        xcnt += board[i].count('X')
    if xcnt > ocnt or ocnt - xcnt > 1:
        return 0

    xwin = is_win('X', board)
    if is_win('O', board):
        if xwin or ocnt - xcnt != 1:
            return 0
    if xwin:
        if ocnt != xcnt:
            return 0

    return 1