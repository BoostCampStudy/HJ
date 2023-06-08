# result
#     correctness: 100.0
#     runtime: 0.01~61.03ms
# key
#     중복검사를 set으로 할 수 없으면 정렬한 리스트로 하기
#     slist에 set을 검사하거나 append하면 이상하게 됨 -> tuple로 감싸기

def dfs(bids, i):
    global sanction, slist, length

    if i == length:
        newb = tuple(sorted(bids))
        if newb not in slist:
            slist.append(newb)
        return

    for item in sanction[i]:
        if item not in bids:
            bids.add(item)
            dfs(bids, i + 1)
            bids.remove(item)

    return


def solution(user_id, banned_id):
    global sanction, slist, length

    length = len(banned_id)
    sanction = [[] for _ in range(length)]  # 불량 사용자별 제재 가능 아이디

    for uid in user_id:
        for i in range(length):
            bid = banned_id[i]

            if len(uid) != len(bid):
                continue

            flag = True
            for j in range(len(bid)):
                if bid[j] == '*':
                    continue
                if bid[j] != uid[j]:
                    flag = False
                    break
            if flag:
                sanction[i].append(uid)

    slist = []
    dfs(set(), 0)

    return len(slist)