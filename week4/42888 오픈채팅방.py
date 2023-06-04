# result:
#     correctness: 100.0
#     runtime: 0.01~104.36ms
# key:
#     순서에 따른 유저 맵핑, 유저에 따른 닉네임 맵핑
#     유저별로 동작을 기록한 후, 마지막에 유저에 따라 닉네임을 추가함

def solution(record):
    mapping = []  # index -> uid
    user = {}  # uid -> nickname
    answer = []
    for string in record:
        action, uid = string.split(" ", 1)

        if action == 'Leave':
            answer.append("님이 나갔습니다.")
            mapping.append(uid)
        else:
            uid, name = uid.split()
            if not user.get(uid) or user.get(uid) != name:
                user[uid] = name

            if action == 'Enter':
                answer.append("님이 들어왔습니다.")
                mapping.append(uid)
            else:
                user[uid] = name

    for i in range(len(mapping)):
        answer[i] = user[mapping[i]] + answer[i]

    return answer