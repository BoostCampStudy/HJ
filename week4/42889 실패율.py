# result
#     correctness: 100.0
#     runtime: 0.01~21.35ms
# key
#     큰 스테이지부터 시작해, 앞선 스테이지에 머물러 있는 사람을 현재에 누적해 1번만 반복하도록
#     dictionary 정렬
#     zip 함수

def solution(N, stages):
    reached = [0 for i in range(N + 1)]
    for n in stages:
        n -= 1
        reached[n] += 1

    uncleared = {}
    for i in range(N - 1, -1, -1):
        un = reached[i] + reached[i + 1]
        if un == 0:
            uncleared[i + 1] = 0
        else:
            uncleared[i + 1] = reached[i] / un
        reached[i] += reached[i + 1]

    uncleared = sorted(uncleared.items())
    uncleared.sort(key=lambda x: x[1], reverse=True)
    ans, _ = zip(*uncleared)

    return ans