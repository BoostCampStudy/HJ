# result
#     correctness: 100.0
# approach
#     중복된 데이터 처리 -> 중복 조건과 python의 directory와 set을 이용
#     k가 1인 경우에 대한 예외처리 (correctness 83.3 -> 100.0)
#     dictionary 혹은 set의 자료를 반환할 때, 데이터 타입 변환

def solution(id_list, report, k):
    rpt = {}
    mail = {}

    for key in id_list:
        mail[key] = 0

    for line in report:
        uid, rid = line.split()
        if rid not in rpt.keys():   # 처음 신고 당한 경우
            rpt[rid] = set()
            rpt[rid].add(uid)
            if k == 1:              # k가 1인 경우, 바로 정지
                mail[uid] += 1
        elif uid not in rpt[rid]:   # 두번째 신고부터는 신고자가 다른 경우에만 신고 접수
                rpt[rid].add(uid)
                l = len(rpt[rid])
                if l == k:          # 이번 신고로 정지되는 경우, 신고자들에게 메일 송신
                    prev_id_list = list(rpt[rid])
                    for key in prev_id_list:
                        mail[key] += 1
                elif l > k:         # 이미 정지된 경우, 새로운 신고자에게 메일 송신
                    mail[uid] += 1

    return list(mail.values())      # dictionay, set 등을 활용한 때는 반환값을 list로 바꾸기