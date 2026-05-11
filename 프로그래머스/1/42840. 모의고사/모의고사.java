import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] answers) {
        int count_1 = 0;
        int count_2 = 0;
        int count_3 = 0;
        
        // 수포자 1의 패턴: 1, 2, 3, 4, 5 반복
        int[] pattern1 = {1, 2, 3, 4, 5};
        // 수포자 2의 패턴: 2, 1, 2, 3, 2, 4, 2, 5 반복
        int[] pattern2 = {2, 1, 2, 3, 2, 4, 2, 5};
        // 수포자 3의 패턴: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 반복
        int[] pattern3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

        // 답안을 비교하며 각 패턴과 비교하여 맞힌 문제를 계산
        for (int i = 0; i < answers.length; i++) {
            if (answers[i] == pattern1[i % pattern1.length]) {
                count_1++;
            }
            if (answers[i] == pattern2[i % pattern2.length]) {
                count_2++;
            }
            if (answers[i] == pattern3[i % pattern3.length]) {
                count_3++;
            }
        }

        // 가장 많은 정답을 맞힌 사람 찾기
        int maxScore = Math.max(count_1, Math.max(count_2, count_3));
        List<Integer> answerList = new ArrayList<>();

        if (count_1 == maxScore) {
            answerList.add(1);
        }
        if (count_2 == maxScore) {
            answerList.add(2);
        }
        if (count_3 == maxScore) {
            answerList.add(3);
        }

        // 리스트를 배열로 변환하여 반환
        int[] answer = new int[answerList.size()];
        for (int i = 0; i < answerList.size(); i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
