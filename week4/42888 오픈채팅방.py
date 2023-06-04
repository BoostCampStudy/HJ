# result:
#     correctness: 100.0
#     runtime: 0.01~123.54ms
# key:
#     순서에 따른 유저 맵핑, 유저에 따른 닉네임 맵핑
#     유저별로 동작을 기록한 후, 마지막에 유저에 따라 닉네임을 추가함
# key!
#     항상 닉네임을 추가하거나 삭제하는 경우만 있어서, 존재하는지 검사할 필요가 없음

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
            user[uid] = name
            if action == 'Enter':
                answer.append("님이 들어왔습니다.")
                mapping.append(uid)

    for i in range(len(mapping)):
        answer[i] = user[mapping[i]] + answer[i]

    return answer