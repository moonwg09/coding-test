using System;

public class Solution {
    public int solution(int n) {
        int H_sum = 0;
        int E_sum = 0;
        if(n % 2 == 0){
            for(int i=2; i<=n; i++){
                if (i % 2 == 0){
                    E_sum += i * i;
                    
                }
            }
            return E_sum;
        }
        else {
            for (int i=1; i<=n; i++){
                if(i % 2 == 1){
                    H_sum += i;
                    
                }
                
            }
            return H_sum;
        }
    }
}