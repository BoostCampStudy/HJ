# result
#     correctness: 100.0
# key
#     원소의 개수가 n인 집합에 a_n이 추가된다

def solution(s):
    string = s[2:-2].split("},{")
    string.sort(key=lambda x: len(x))

    answer = []
    for s in string:
        for n in map(int, s.split(",")):
            if n not in answer:
                answer.append(n)

    return answer