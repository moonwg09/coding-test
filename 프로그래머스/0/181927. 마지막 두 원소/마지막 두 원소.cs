using System;

public class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.Length;
        int last = num_list[len - 1];
        int prev = num_list[len - 2];
        
        int nextValue = (last > prev) ? (last - prev) : (last * 2);
        
        int[] answer = new int[len + 1];
        Array.Copy(num_list, answer, len);
        answer[len] = nextValue;
        
        return answer;
    }
}