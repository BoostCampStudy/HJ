# result
#     correctness 100.0
#     runtime: 0.02~0.17ms, 0.85ms
# key
#     다중집합의 교집합 -> dictionary로 카운팅해서 세기
#     딕셔너리의 get 메소드 활용하여 에러 없이 교집합 검사
#     <- 딕셔너리를 loop할 때는, del 키워드 사용 불가 (루프 중 딕셔너리 길이 변화가 생기면 안 됨)
#     jset을 만들면서 keys 배열을 만들면 del을 써도 될 것 같은데?

def get_jset(string, jset):
    for i in range(len(string) - 1):
        c = string[i:i + 2]
        if c.isalpha():
            if jset.get(c):
                jset[c] += 1
            else:
                jset[c] = 1

    return


def solution(str1, str2):
    jset1 = {}
    jset2 = {}

    get_jset(str1.lower(), jset1)
    get_jset(str2.lower(), jset2)

    inter = union = 0
    if jset1 or jset2:
        for k in jset1:
            while jset1[k] != 0 and jset2.get(k, 0) != 0:
                jset1[k] -= 1
                jset2[k] -= 1
                inter += 1
                union += 1
            union += jset1[k]
            jset1[k] = 0
            if jset2.get(k, 0) != 0:
                union += jset2[k]
                jset2[k] = 0

        for k in jset2:
            if jset2[k] != 0:
                union += jset2[k]
                jset2[k] = 0

        j = inter / union
    else:
        j = 1

    return int(j * 65536)