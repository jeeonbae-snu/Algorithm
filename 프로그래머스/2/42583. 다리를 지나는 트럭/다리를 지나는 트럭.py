from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리의 상태 (트럭의 무게로 초기화)
    total_weight = 0  # 현재 다리 위의 총 중량
    queue = deque(truck_weights)  # 대기 중인 트럭들
    
    while queue:
        time += 1
        # 다리의 앞쪽 트럭이 다리를 다 건너면 제거
        total_weight -= bridge.popleft()
        
        # 다음 트럭을 다리에 올릴 수 있는지 확인
        if queue:
            if total_weight + queue[0] <= weight:
                truck = queue.popleft()
                bridge.append(truck)  # 다리에 트럭 추가
                total_weight += truck  # 총 중량 업데이트
            else:
                bridge.append(0)  # 다리에는 트럭을 추가하지 않음
        
    return time + bridge_length  # 마지막 트럭이 다리의 끝에 도달할 때까지 추가 시간