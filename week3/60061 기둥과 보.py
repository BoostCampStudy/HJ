# result
#     correctness: 9.6/100.0


def solution(n, build_frame):
    frame = [[[False, False] for j in range(n + 1)] for i in range(n + 1)]
    for info in build_frame:
        x, y, is_girder, is_build = info
        flag = False

        if is_girder:
            # 보 설치
            if is_build:
                if (frame[x][y - 1][0] or frame[x + 1][y - 1][0]) \
                        or (frame[x - 1][y][1] and frame[x + 1][y][1]):
                    frame[x][y][1] = True
            # 보 삭제  -> y는 0이 아니고, x는 n이 아님
            else:
                # 왼쪽에 보 존재
                # x-1, y-1이나 x, y-1에 기둥이 있어야
                if x != 0 and frame[x - 1][y][1]:
                    flag = True
                    if frame[x - 1][y - 1][0] or frame[x][y - 1][0]:
                        flag = False
                if flag:
                    continue

                # 오른쪽에 보 존재
                # x+1, y-1이나 x+2, y-1에 기둥이 있어야
                if x != n - 1 and frame[x + 1][y][1]:
                    flag = True
                    if frame[x + 1][y - 1][0] or frame[x + 2][y - 1][0]:
                        flag = False
                if flag:
                    continue
                # 위에 기둥 존재
                # x, y-1에 기둥이 있거나, x-1, y에 보가 있어야
                if frame[x][y][0]:
                    flag = True
                    if (frame[x][y - 1][0] or (x != 0 and frame[x - 1][y][1])):
                        flag = False

                if flag is False:
                    frame[x][y][1] = False

        else:
            # 기둥 설치
            if is_build:
                if (y == 0 or frame[x][y - 1][0]) \
                        or (x != 0 and frame[x - 1][y][1]) or (x != n and frame[x][y][1]):
                    frame[x][y][0] = True

            # 기둥 삭제
            else:
                # 오른쪽 위(x, y+1)에 보 존재 -> x는 n이 아님
                # x+1, y에 기둥이 있거나, x-1, y+1과 x+1, y+1에 보가 있어야 ㅎ함
                if frame[x][y + 1][1]:
                    flag = True
                    if x == 0 and frame[x + 1][y][0]:
                        flag = False
                    elif (frame[x + 1][y][0]) or (frame[x - 1][y + 1][1] and frame[x + 1][y + 1][1]):
                        flag = False
                if flag:
                    continue

                # 왼쪽 위에 보 존재
                # x-1, y에 기둥이 있거나, x-2, y+1과 x, y+1에 보가 있어야
                if x != 0 and frame[x - 1][y + 1][1]:
                    flag = True
                    if frame[x - 1][y][0] or ((x != 1 and frame[x - 2][y + 1][1]) and (x != n and frame[x][y + 1][1])):
                        flag = False
                if flag:
                    continue
                # 위에 기둥 존재
                # x, y+1이나 x-1, y+1에 보가 있어야
                if y != n - 1 and frame[x][y + 1][0]:
                    flag = True
                    if ((x != n and frame[x][y + 1][0]) or (x != 0 and frame[x - 1][y + 1][1])):
                        flag = False

                if flag is False:
                    frame[x][y][1] = False

    answer = []
    for i in range(n):
        for j in range(n):
            if frame[i][j][0]:
                l = [i, j, 0]
                answer.append(l)
            if frame[i][j][1]:
                l = [i, j, 1]
                answer.append(l)
    print(frame)

    return answer
