# result
#     correctness: 100.0
# key
#     split()의 파라미터로 '0'을 넘겨줄 시, '1001'은 '1' '' '1'로 분리됨
#     1. while문과 replace()로 '00'을 '0'으로 대체
#     2. k진수로 변환하는 과정에서 0 처리


import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    prev = ""
    words = []
    while n > k:
        if n % k == 0:
            if prev != "":
                words.append(prev)
                prev = ""
        else:
            prev = str(n % k) + prev

        n //= k

    if n != 0:
        if prev != "":
            words.append(str(n) + prev)
        else:
            words.append(str(n))

    answer = 0
    for word in words:
        if word != '1' and is_prime(int(word)):
            answer += 1

    return answer