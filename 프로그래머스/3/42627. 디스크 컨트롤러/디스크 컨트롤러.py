def solution(jobs):
    # 작업을 요청 시점으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    current_time = 0  # 현재 시간
    wait_time = 0  # 총 대기 시간
    n = len(jobs)  # 작업의 총 개수
    job_index = 0  # 현재 작업 인덱스
    queue = []  # 대기 중인 작업을 저장하는 리스트

    while job_index < n or queue:
        # 현재 시간에 도착한 작업을 큐에 추가
        while job_index < n and jobs[job_index][0] <= current_time:
            queue.append(jobs[job_index])
            job_index += 1
        
        if queue:
            # 대기 중인 작업 중 가장 짧은 작업 선택
            queue.sort(key=lambda x: x[1])  # 소요시간 기준으로 정렬
            current_job = queue.pop(0)  # 가장 짧은 작업 선택
            current_time += current_job[1]  # 현재 시간을 업데이트
            wait_time += current_time - current_job[0]  # 대기 시간 계산
        else:
            # 큐가 비어 있다면, 다음 작업의 요청 시점까지 현재 시간을 업데이트
            current_time = jobs[job_index][0]  # 다음 작업의 요청 시점으로 이동

    # 평균 대기 시간 계산 (소수점 이하 버림)
    return wait_time // n

print(solution([[0, 3], [1, 9], [2, 6]]))  # 예시 출력
