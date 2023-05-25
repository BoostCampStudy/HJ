# result
#     correctness: 100.0
# key
#     문자열 슬라이싱
#     날짜 사이의 선후 계산

def get_integer(string):
    return int(string) if string[0] != '0' else int(string[1:])


def solution(today, terms, privacies):
    y, m, d = map(get_integer, today.split("."))

    dest_day = {}
    for data in terms:
        kind, term = data.split()
        term = int(term)

        q = term // 12
        r = term % 12
        if m > r:
            dest_day[kind] = (y - q, m - r, d)
        else:
            dest_day[kind] = (y - q - 1, 12 + m - r, d)

    answer = []
    for i in range(len(privacies)):
        data, kind = privacies[i].split()
        y, m, d = map(get_integer, data.split("."))
        dy, dm, dd = dest_day[kind]

        # dest_day 포함 이전의 자료는 폐기
        if y < dy:
            answer.append(i + 1)
        if y == dy and m < dm:
            answer.append(i + 1)
        if y == dy and m == dm and d <= dd:
            answer.append(i + 1)

    return answer