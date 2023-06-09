# result
#     correctness: 100.0
#     runtime: 0.01~0.61ms
# key
#     중간에 입력 문자열의 삭제가 발생하므로 for문보단 while로 반복
#     i & j의 종료 조건
#     python의 len()은 O(1)로, 객체의 길이를 따로 변수에 저장하는 것과 큰 차이는 없다!
# key!
#     dict.keys()로 방문한 게 마음에 안 드는데...
#     -> 집합을 추가해 봤는데, 몇몇 케이스가 0.1ms정도 빨라지나 최악의 경우 0.96ms 수행함
#     -> 해싱 두 개 하는 건 메모리적으로도 일반성을 위해서라도 별로인 듯?

def solution(msg):
    zipdict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
               'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23,
               'X': 24, 'Y': 25, 'Z': 26}
    length = len(msg)
    cnt = 27
    i = 0
    answer = []
    while i < length:
        j = i + 1
        while msg[i:j] in zipdict.keys() and j < length + 1:
            j += 1

        answer.append(zipdict[msg[i:j - 1]])
        zipdict[msg[i:j]] = cnt
        cnt += 1
        i = j - 1

    return answer