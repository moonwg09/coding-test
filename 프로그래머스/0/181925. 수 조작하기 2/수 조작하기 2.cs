using System;
using System.Text;

public class Solution {
    public string solution(int[] numLog) {
        StringBuilder sb = new StringBuilder();
        
        for (int i = 1; i < numLog.Length; i++) {
            int diff = numLog[i] - numLog[i - 1];
            
            sb.Append(diff switch {
                1 => 'w',
                -1 => 's',
                10 => 'd',
                -10 => 'a',
                _ => ""
            });
        }
        
        return sb.ToString();
    }
}