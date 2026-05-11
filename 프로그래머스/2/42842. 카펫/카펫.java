import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int brown, int yellow) {
        List<Integer> heigths = new ArrayList<>();
        
        for(int i = 1; i <= (int) Math.sqrt(yellow); i++){
            if(yellow % i == 0){
                heigths.add(i);
            }
        }
        
        List<Integer> widths = new ArrayList<>();
        for (int h: heigths){
            widths.add(yellow/h);
        }
        
        for(int i = 0; i < heigths.size(); i++){
            int heigth = heigths.get(i);
            int width = widths.get(i);
            if (2 * width + 2 * heigth + 4 == brown){
                return new int[]{width + 2, heigth + 2};
            }
        }
        return new int[]{-1, -1};
    }
}

