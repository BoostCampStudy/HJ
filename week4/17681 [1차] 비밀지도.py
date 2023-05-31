# result
#     correctness: 100.0
#     runtime: 0.02~0.14ms
# key
#     str 객체에는 sort()가 지원되지 않으므로, 리버스는 문자열 슬라이싱 활용
#     이진수와 주어진 길이를 비교하여 leading zero 채우기


def decode(num, n):
    result = ''
    while num > 0:
        if num % 2 == 0:
            result += ' '
        else:
            result += '#'
        num //= 2

    result = result[::-1]
    result = ' ' * (n - len(result)) + result

    return result


def solution(n, arr1, arr2):
    answer = ['' for i in range(n)]

    for i in range(n):
        line1 = decode(arr1[i], n)
        line2 = decode(arr2[i], n)
        for j in range(n):
            answer[i] += line1[j] if line1[j] == line2[j] else '#'

    return answer