def solution(routes):
    # 구간을 끝 지점을 기준으로 정렬
    routes.sort(key=lambda x: x[1])
    ans = 0
    last_camera = -30001  # 카메라가 설치된 마지막 위치 (충분히 작은 수로 초기화)

    for route in routes:
        # 현재 구간의 시작 지점이 마지막 카메라 위치보다 크면 새 카메라 설치
        if route[0] > last_camera:
            ans += 1
            last_camera = route[1]  # 현재 구간의 끝 지점에 카메라 설치

    return ans

