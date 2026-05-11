from itertools import permutations

def tsp(n, cost_matrix):
    min_cost = float('inf')  # 최소 비용을 무한대로 초기화
    cities = range(n)  # 0부터 n-1까지 도시 리스트 생성
    
    # 모든 도시 순열(경로)을 확인
    for perm in permutations(cities):
        current_cost = 0
        valid_path = True
        
        # 경로에 따른 비용 계산
        for i in range(n - 1):
            if cost_matrix[perm[i]][perm[i + 1]] == 0:  # 연결되지 않은 경로 처리
                valid_path = False
                break
            current_cost += cost_matrix[perm[i]][perm[i + 1]]
        
        # 마지막 도시에서 시작 도시로 돌아오는 비용 추가
        if valid_path and cost_matrix[perm[-1]][perm[0]] > 0:
            current_cost += cost_matrix[perm[-1]][perm[0]]
            min_cost = min(min_cost, current_cost)
    
    return min_cost

# 입력 처리
n = int(input())
cost_matrix = [[int(x) for x in input().split()] for _ in range(n)]

# 최소 비용 계산
min_cost = tsp(n, cost_matrix)
print(min_cost)
