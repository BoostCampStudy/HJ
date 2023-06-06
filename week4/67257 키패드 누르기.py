# result
#     correctness: 100.0
#     runtime: 0.01~0.32ms

def solution(numbers, hand):
    pos = {}
    for i in range(3):
        for j in range(1, 4):
            pos[i * 3 + j] = (i, j - 1)
    pos[0] = (3, 1)

    ans = ''
    li = ri = 3
    lj, rj = 0, 2
    for n in numbers:
        if n in [1, 4, 7]:
            li, lj = pos[n]
            ans += 'L'
        elif n in [3, 6, 9]:
            ri, rj = pos[n]
            ans += 'R'
        else:
            i, j = pos[n]
            ldist = abs(li - i) + abs(lj - j)
            rdist = abs(ri - i) + abs(rj - j)

            if ldist < rdist:
                li, lj = pos[n]
                ans += 'L'
            elif ldist > rdist:
                ri, rj = pos[n]
                ans += 'R'

            elif hand == 'left':
                li, lj = pos[n]
                ans += 'L'
            else:
                ri, rj = pos[n]
                ans += 'R'

    return ans