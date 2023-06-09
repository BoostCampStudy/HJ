# result
#     correctness: 100.0
#     runtime: 0.01~0.48ms
# key
#     Nonetype은 packing return 불가능
#     간단한 for 반복은 map과 lambda 고민해보기

def get_uv(w):
    ocnt = ccnt = 0
    for i in range(len(w)):
        if w[i] == '(':
            ocnt += 1
        else:
            ccnt += 1

        if i != 0 and ocnt == ccnt:
            return w[:i + 1], w[i + 1:]


def is_correct(u):
    n = 0
    for c in u:
        if c == '(':
            n += 1
        else:
            if n == 0:
                return False
            n -= 1

    return True


def solution(p):
    if p == "":
        return p

    u, v = get_uv(p)

    if is_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + "".join(map(lambda x: ')' if x == '(' else '(', u[1:-1]))