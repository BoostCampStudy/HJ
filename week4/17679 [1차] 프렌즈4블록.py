# result
#     correctness: 100.0
#     runtime: 0.03~304.45ms
# key
#     문자열은 대입 연산자가 불가능하므로 슬라이싱 or 사전에 char형의 배열로 처리


def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])

    ans = 0
    while True:
        deleted = set()
        for i in range(m):
            for j in range(n):
                if i == m - 1 or j == n - 1 or board[i][j] == '-':
                    continue

                flag = True
                for di in range(2):
                    for dj in range(2):
                        if board[i + di][j + dj] != board[i][j]:
                            flag = False
                if flag:
                    deleted.add((i, j))
                    deleted.add((i + 1, j))
                    deleted.add((i, j + 1))
                    deleted.add((i + 1, j + 1))

        if not deleted:
            break

        for i, j in deleted:
            board[i][j] = '-'
            ans += 1

        for j in range(n):
            for i in range(m - 1, 0, -1):
                if board[i][j] == '-':
                    newi = i - 1
                    while newi >= 0:
                        if board[newi][j] != '-':
                            break
                        newi -= 1

                    if newi != -1:
                        board[i][j] = board[newi][j]
                        board[newi][j] = '-'

    return ans