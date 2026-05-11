def solution(progresses, speeds):
    Q = []
    
    for progress, speed in zip(progresses, speeds):
        # 작업이 완료되는 데 걸리는 시간 계산
        completion_time = -((progress - 100) // speed)
        
        if len(Q) == 0 or Q[-1][0] < completion_time:
            Q.append([completion_time, 1])  # 새로운 그룹 추가
        else:
            Q[-1][1] += 1  # 기존 그룹의 배포 수 증가
    
    return [q[1] for q in Q]  # 배포 수 리스트 반환

