# result
#     correctness: 100.0
#     runtime: 0.03~4.42ms
# key
#     정렬 기준에 쓰일 문자열을 따로 슬라이싱해두고, 순서로 매핑
#     나도 정규식 쓰고 싶다...


def solution(files):
    sfiles = []
    for i in range(len(files)):
        s = files[i]
        head = num = tail = None
        for j in range(len(s)):
            if s[j].isdigit():
                head = s[:j]
                num = s[j:]
                break
        for j in range(len(num)):
            if j > 5 or not num[j].isdigit():
                num = num[:j]
                break
        sfiles.append([head.lower(), int(num), i])

    sfiles.sort(key=lambda x: (x[0], x[1]))

    answer = []
    for sfile in sfiles:
        _, _, index = sfile
        answer.append(files[index])

    return answer