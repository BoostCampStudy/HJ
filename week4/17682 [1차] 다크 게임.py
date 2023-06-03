# result
#     correctness: 100.0
#     runtime: 0.02~0.05
# key
#     정수간의 power 연산은 ** 연산자가 더 정확함

def solution(dartResult):
    scores = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    prev_num = ''
    for c in dartResult:
        if c.isdigit():
            prev_num += c

        elif c in bonus.keys():
            scores.append(int(prev_num))
            prev_num = ''
            scores[-1] = scores[-1] ** bonus[c]

        elif c == '*':
            if len(scores) == 1:
                scores[0] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
        elif c == '#':
            scores[-1] *= (-1)

    return sum(scores)