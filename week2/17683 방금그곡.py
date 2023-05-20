# result
#   correctness: 36.7 (time over)
# approach
#   재생된 시간 만큼 sheet의 길이를 줄이거나 반복하며 늘림
#   m이 조정한 sheet에 존재하는지 확인


def get_miniute(string):
    h, m = string.split(":")
    if h[0] == '0':
        h = h[1]
    if m[0] == '0':
        m = m[1]
    return int(h) * 60 + int(m)


def convert_melody(sheet):
    convert_map = {"C#": 'c', "D#": 'd', "F#": 'f', "G#": 'g', "A#": 'a'}
    for k in convert_map.keys():
        sheet = sheet.replace(k, convert_map[k])

    return sheet


def solution(m, musicinfos):
    m = convert_melody(m)
    max_playtime = -1
    max_name = "(None)"
    for music in musicinfos:
        start, end, name, sheet = music.split(",")
        playtime = get_miniute(end) - get_miniute(start)
        sheet = convert_melody(sheet)
        los = len(sheet)
        if playtime < los:
            sheet = sheet[:playtime]
        elif playtime > los:
            gap = playtime - los
            for _ in range(gap // los):
                sheet += sheet
            sheet += sheet[:gap % los]

        if m in sheet and playtime > max_playtime:
            max_playtime = playtime
            max_name = name

    return max_name