# result
#     correctness: 100.0
# key
#     거리두기가 지켜지지 않는 케이스는 3개로 나눈 후, 각각 검사
#     place의 개수와 크기가 모두 5, 5*5로 제한되어 방문 기록을 하지 않아도 됨


def solution(places):
    straigh1 = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    straigh2 = [(2, 0), (-2, 0), (0, 2), (0, -2)]
    diagnal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    answer = []
    for place in places:
        people = set()
        part = set()
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.add((i, j))
                elif place[i][j] == 'X':
                    part.add((i, j))

        flag = False
        for p in people:
            pi, pj = p
            for d in straigh1:  # 두 응시자간의 거리가 1
                dx, dy = d
                if (pi + dx, pj + dy) in people:
                    flag = True
                    break
            if flag:
                break

            for d in straigh2:  # 두 응시자간의 거리가 직선으로 2이고 둘 사이에 파티션이 없는 경우
                dx, dy = d
                if (pi + dx, pj + dy) in people:
                    if (pi + (dx // 2), pj + (dy // 2)) not in part:
                        flag = True
                        break
            if flag:
                break

            for d in diagnal:  # 두 응시자간의 거리가 대각선으로 2이고, 양쪽 중 하나라도 파티션이 없는 경우
                dx, dy = d
                if (pi + dx, pj + dy) in people:
                    if (pi + dx, pj + 0) not in part or (pi + 0, pj + dy) not in part:
                        flag = True
                        break

        if flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer