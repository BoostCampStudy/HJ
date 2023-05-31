# result
#   correctness: 100.0
#   runtime: 0.02 ~ 0.04ms
# key
#   dictionary 와 replace를 활용하여 반복 시간 줄이기


def solution(s):
    stoi = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6' \
        , 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'}

    for k, v in stoi.items():
        s = s.replace(k, v)

    return int(s)