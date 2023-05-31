# result
#   correctness: 100.0
#   runtime: 0.03 ~ 0.07ms
# Cons
#   dictionary 제대로 활용하지 못한 느낌


def solution(s):
    stoi = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6' \
        , 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}
    answer = ''

    history = ''
    for c in s:
        if c in stoi.values():
            answer += c
        else:
            history += c
            if history in stoi.keys():
                answer += stoi[history]
                history = ''

    return int(answer)