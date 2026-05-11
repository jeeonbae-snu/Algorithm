class Solution {
        // DFS를 사용하여 가능한 최대 던전 탐험 수를 계산
    public int dfs(int k, int[][] dungeons, boolean[] visited, int count) {
        int maxCount = count;  // 현재 탐색에서 가능한 최대 던전 수

        // 모든 던전 탐색
        for (int i = 0; i < dungeons.length; i++) {
            // 던전을 아직 방문하지 않았고, 피로도가 충분하다면
            if (!visited[i] && dungeons[i][0] <= k) {
                visited[i] = true;  // 해당 던전을 방문한 것으로 표시
                maxCount = Math.max(maxCount, dfs(k - dungeons[i][1], dungeons, visited, count + 1));  // 재귀 호출
                visited[i] = false;  // 방문 여부 복구
            }
        }

        return maxCount;
    }

    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];  // 던전 방문 여부를 추적하기 위한 배열
        return dfs(k, dungeons, visited, 0);  // DFS 시작
    }
}