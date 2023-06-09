# result
#     correctness: 100.0
#     runtime: 0.05~0.27ms
# key
#     리스트 복사시 카피하는 거 잊지 않기


from itertools import permutations


def slice_exp(e):
    num = ""
    exp = []
    for i in range(len(e)):
        if e[i].isdigit():
            num += e[i]
        else:
            exp.append(int(num))
            exp.append(e[i])
            num = ""

    exp.append(int(num))

    return exp


def calculate(exp, op):
    j = 0
    while j < len(exp):
        if exp[j] != op:
            j += 1
        else:
            exp.pop(j)
            if op == '+':
                exp.insert(j - 1, exp.pop(j - 1) + exp.pop(j - 1))
            elif op == '-':
                exp.insert(j - 1, exp.pop(j - 1) - exp.pop(j - 1))
            else:
                exp.insert(j - 1, exp.pop(j - 1) * exp.pop(j - 1))

    return


def solution(expression):
    priority = list(permutations(('+', '-', '*')))

    exp = slice_exp(expression)

    results = []
    for i in range(6):
        newe = exp.copy()
        for op in priority[i]:
            calculate(newe, op)
        results.append(abs(newe[0]))

    return max(results)