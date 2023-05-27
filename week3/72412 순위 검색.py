# result
#     correctness: 40.0
#     efficiency: 0.0
#     total: 40.0 / 100.0
# Cons
# 1. hashing이 2번 (딕셔너리 안에 집합)
# 2. 최악의 경우 O(n^2)

def solution(info, query):
    pl = {"java": set(), "python": set(), "cpp": set(), "-": set()}
    job = {"backend": set(), "frontend": set(), "-": set()}
    career = {"junior": set(), "senior": set(), "-": set()}
    food = {"chicken": set(), "pizza": set(), "-": set()}
    score = []
    answer = []

    for i in range(len(info)):
        p, j, c, f, s = info[i].split()
        pl[p].add(i)
        job[j].add(i)
        career[c].add(i)
        food[f].add(i)

        pl["-"].add(i)
        job["-"].add(i)
        career["-"].add(i)
        food["-"].add(i)

        score.append(int(s))

    for q in query:
        p, j, c, f = q.split(" and ")
        f, s = f.split()

        s = int(s)
        inter = pl[p] & job[j] & career[c] & food[f]
        cnt = 0
        if inter:
            for i in inter:
                if score[i] >= s:
                    cnt += 1

        answer.append(cnt)

    return answer