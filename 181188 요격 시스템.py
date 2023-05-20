# result
#   corectness: 100.0
# approach
#   구간이 주어진 targets들 사이의 겹치는 구간의 개수 찾기
#    1. 기존의 미사일과 범위가 겹치는 경우: 최소한의 범위로 축소
#    2. 기존의 미사일과 범위가 겹치지 않는 경우: 새로운 미사일 추가
#    targets를 정렬하여 범위를 비교하면, 가장 최근의 미사일과만 비교할 수 있음

def solution(targets):
    targets.sort(key=lambda x: x[0])

    missiles = [targets[0]]
    for s, e in targets[1:]:
        m = missiles[-1]
        if not ((s <= m[0] and e <= m[0]) or (s >= m[1] and e >= m[1])):
            m[0] = max(s, m[0])
            m[1] = min(e, m[1])
        else:
            missiles.append([s, e])

    return len(missiles)
