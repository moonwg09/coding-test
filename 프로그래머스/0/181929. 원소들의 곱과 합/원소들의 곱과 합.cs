using System;

public class Solution {
    public int solution(int[] num_list) {
        int mul = 1;
        int sum = 0;
        
        for (int i=0; i<num_list.Length; i++){
            mul *= num_list[i];
            sum += num_list[i];
        }
        
        if(mul>sum*sum){
            return 0;
        }
        else{
            return 1;
        }
    }
}