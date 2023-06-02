# result
#     corectness: 100.0
#     runtime: 0.00~1.10ms, 115.79ms
# key
#     캐시가 존재하지 않는 경우 예외 처리
#     dictionary 검색 (키 참조와 get, del과 .pop()의 차이)

def solution(cacheSize, cities):
    cache = {}
    runtime = 0
    time = 0

    if cacheSize == 0:      # 캐시가 존재하지 않는 경우
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in cache.keys():    # hit
            runtime += 1
        else:                       # miss
            runtime += 5
            if len(cache.keys()) == cacheSize:  # least recently used
                m = min(cache.values())
                for c, t in cache.items():
                    if t == m:
                        del cache[c]
                        break

        cache[city] = time
        time += 1

    return runtime