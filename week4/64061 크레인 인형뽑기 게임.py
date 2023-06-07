# result
#     correctness: 100.0
#     runtime: 0.01~0.29ms
# key
#     board의 각 열을 stack으로 취급 -> 각각의 top을 관리하여 탐색 범위 축소
#     bascket에서의 삭제는 새로운 값이 추가될 때만 1회 발생할 수 있음

def solution(board, moves):
    N = len(board[0])
    top = []
    for j in range(N):
        for i in range(N):
            if board[i][j] != 0:
                top.append(i)
                break
        if len(top) != j + 1:
            top.append(0)

    ans = 0
    bascket = []
    for m in moves:
        m -= 1
        if top[m] < N:
            bascket.append(board[top[m]][m])
            top[m] += 1

            if len(bascket) > 1 and bascket[-1] == bascket[-2]:
                bascket.pop()
                bascket.pop()
                ans += 2

    return ans