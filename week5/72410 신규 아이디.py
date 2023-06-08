# result
#     correctness: 100.0
#     runtime: 0.01~0.32ms
# key
#     반복문을 돌며 문자열의 부분을 편집하기 힘들면 ''에 +=하는 방법 떠올리기


def solution(new_id):
    recommend = ''
    for c in new_id.lower():  # 1
        if c.isalnum() or c in ['-', '_', '.']:  # 2
            if recommend and c == '.' and recommend[-1] == '.':  # 3
                continue
            recommend += c

    # 4
    if recommend:
        if recommend == '.':
            recommend = ''
        else:
            if recommend[0] == '.':
                recommend = recommend[1:]
            if recommend[-1] == '.':
                recommend = recommend[:-1]

    # 5
    if not recommend:
        recommend = 'a'
    # 6
    elif len(recommend) > 15:
        if recommend[14] == '.':
            recommend = recommend[:14]
        else:
            recommend = recommend[:15]

    # 7
    if len(recommend) < 3:
        recommend += recommend[-1] * (3 - len(recommend))

    return recommend