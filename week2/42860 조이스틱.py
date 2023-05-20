# result
#   correctness: 100.0
# approach
#   axaaaaaajaa 와 같은 case 때문에 왼쪽으로 갔다가 오른쪽으로 돌아오는 경우 필요함 == 방문 확인 힘듦
#   worst case: 0부터 l-1까지 순회하는 경우 -> l은 최대 20이므로, 최악의 실행은 2^2 = 1,048,576번 수행
#   즉, 왔다갔다하는 무한 반복에 빠져도 짧은 시간 안에 해결 가능한
#   방문 확인 없이 BFS로 풀이 가능


from collections import deque


def solution(name):
    answer = 0
    for c in name:
        answer += min(ord(c) - ord('A'), ord('Z') - ord(c) + 1)

    l = len(name)
    all_a = 'A' * l
    queue = deque()
    queue.append((name, 0, 0))
    while queue:
        string, i, m = queue.popleft()
        if string[i] != 'A':
            if i != l - 1:
                string = string[:i] + 'A' + string[i + 1:]
            else:
                string = string[:i] + 'A'
        if string == all_a:
            answer += m
            break

        if i != l - 1:
            queue.append((string, i + 1, m + 1))
        else:
            queue.append((string, 0, m + 1))

        if i != 0:
            queue.append((string, i - 1, m + 1))
        else:
            queue.append((string, l - 1, m + 1))

    return answer